from bs4 import BeautifulSoup
import requests as req
import re
from filter_urls import find_articles, find_urls
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def extract_team_data(url):
    """Takes a url and finds the team roster, extracts all the links from the url roster table column corresponding to players.
    Takes alle the links to player wikis and requests player data for all players, players with adequate statistics get stats added to a list.
    This list is then returned

    Args:
        url (str)       : A String consisting of a wikipedia url for a basketball team

    Returns:
        list            : List of all the team players data
    """
    data = req.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    a = str(soup.title)

    pat = r"(?<=20 )(.*?)(?= season)"
    team = re.findall(pat, a, re.S)
    print(team)
    pat = r"(?<=Roster)(.*?)(?=Standings)"
    re_data = re.findall(pat, data.text, re.S)
    soup = BeautifulSoup(re_data[1], "html.parser")

    soup_table = soup.find_all("table", class_="sortable")

    players = []
    for items in soup_table:
        line = items.find_all(["tr"])
        # print(line[1])
        for i in range(len(line)):
            a = extract_player_data(str(line[i]), team[0])

            if len(a) > 5:
                players.append(a)

    return players


def extract_player_data(string, team):

    """Takes a string consisting the link of a basketball player, finds the correct url.
       Then finds the table for player statistics and extracts the 2019/2020 season.
       The statistics is added to a list and returns it.

    Args:
        string (str)       : A String consisting of a table line from a team roster
        team (str)      : Name of the team the player represents

    Returns:
        list            : List of the player statistisc for the 2019/2020 season
    """

    urls = find_urls(string)
    artics = find_articles(urls)

    # Some lines of the table have zero urls and have to be skipped
    if len(artics) < 1:
        return [0]  # Will be discarded by caller function¨

    # Finding player statistics table

    data = req.get(artics[1])
    soup = BeautifulSoup(data.text, "html.parser")
    soup_table = soup.find_all("table", class_="sortable")

    # Finds name in order to add to list.

    a = str(soup.title)

    pat = r"(?<=\<title\>)(.*?)(?= \-)"
    name = re.findall(pat, a, re.S)
    # Some players have no data for this season and have to be skipped
    try:
        stats = str(soup_table[0])
    except:
        print("Error for player: " + name[0])
        return [0]

    # For pattern, 2019 is found first in the relevant line of the table, and Career statistics is the first string of the next line, relevant info is in between

    pat = r"(?<=2019)(.*?)(?=Career)"
    re_data = re.findall(pat, stats, re.S)

    # Breaks ut the line into a list of info found in each cell of the table row
    pat = r"(?<=\<td\>|\<td )(.*?)(?=\<\/td|\\)"
    numbs = re.findall(pat, str(re_data), re.S)

    # Declearing variable to be returned, ads name and team
    returned_stats = [name[0], team]

    # Some players switched teams during the season, this test results in only the last team played for is extracted
    if len(numbs) == 25:

        a = []
        for i in range(14, 25):
            a.append(numbs[i])
        numbs = a

    # Appending statistics to returned variable
    # Due to several variations of writing in the player statistics (Such as using bold text of "*") the method consists of several try/except statements
    for n in numbs:
        try:
            a = float(n)
            returned_stats.append(a)
        except:

            try:
                pat = r"(?<=b\>|\"\>)(.*?)(?=\<|\*)"
                num = re.findall(pat, n, re.S)
                returned_stats.append(float(num[0]))

            except:
                if str(n) == "–" or str(n) == "—" or str(n) == "-":
                    returned_stats.append(0.00001)

                else:
                    try:
                        pat = r"(?<=b\>)(.*?)(?=\<)"
                        num = re.findall(pat, n, re.S)
                        returned_stats.append(float(num[0]))
                    except:
                        # print(n)
                        pass

    if len(returned_stats) == 12:
        # Some players have no data for number of games started, this seamed to be the only instance where a player had 10 entries in table
        # This is a quick fix, and could lead to some severe bugs, if PPG, BPG or RPG is missing and the lines shifts. One way then to solve would be to discard
        returned_stats.insert(3, 0)

    return returned_stats


# _____________________________________________________________________________________________
# Initiation

url = "https://en.wikipedia.org/wiki/2020_NBA_playoffs"

# Extracts the bracket part of the link due to many tables in link
data = req.get(url)
pat = r"(?<=Bracket)(.*?)(?=Play\-in game)"
re_data = re.findall(pat, data.text, re.S)

# Bracket table is now the only in the string, no need to search
soup = BeautifulSoup(re_data[1], "html.parser")
soup_table = soup.find_all("table")

# Finding the team articles in bracket table
urls = find_urls(str(soup_table[0]))
artics = find_articles(urls)

# Filtering out the links not to team season articles, luckily all end with the string "season"
teams = []
for a in artics:
    if a[-6:] == "season":
        teams.append(a)

# ____________________________________________________________________________________________

# Semifinalists found manually.
semifinalists = [0, 3, 4, 6, 8, 10, 12, 14]

# Color ID for each team, dictionary created to link team number with color
color_id = ["0", "3", "4", "6", "8", "10", "12", "14"]
color_list = ["b", "g", "r", "c", "m", "y", "k", "tan"]
d2c = dict(zip(color_id, color_list))

# Creating separate dataframes for each stat analyzed
PPG_df = pd.DataFrame()
BPG_df = pd.DataFrame()
RPG_df = pd.DataFrame()

# Obtaining team data for each team
for i in range(len(semifinalists)):

    # Obtaining a matrix of the team's players statistics
    stats = []
    pl = extract_team_data(teams[semifinalists[i]])
    stats.append(pl)
    arr = np.array(stats)
    mat = np.matrix(arr[0])

    headers = [
        "Player",
        "Team",
        "GP",
        "GS",
        "MPG",
        "FG%",
        "3P%",
        "FT%",
        "RPG",
        "APG",
        "SPG",
        "BPG",
        "PPG",
    ]

    # Converting matrix to pandas dataframe
    df = pd.DataFrame(mat, columns=headers)

    # Inserting color column with a color key, all players of same team will have same color key
    df["color"] = color_id[i]

    # Sorting by columns and adding the top 3 from each team to a separate dataframe
    df["PPG"] = df["PPG"].astype(float)
    adf = df.sort_values(["PPG"], ascending=False)

    PPG_df = PPG_df.append(adf.iloc[0:3])

    df["BPG"] = df["BPG"].astype(float)
    adf = df.sort_values(["BPG"], ascending=False)
    BPG_df = BPG_df.append(adf.iloc[0:3])

    df["RPG"] = df["RPG"].astype(float)
    adf = df.sort_values(["RPG"], ascending=False)
    RPG_df = RPG_df.append(adf.iloc[0:3])

# Plotting each of the dataframes

import matplotlib.patches as mpatches

# Legend is created using a hardcoded approach
b_patch = mpatches.Patch(color="b", label="Milwaukee Bucks")
g_patch = mpatches.Patch(color="g", label="Indiana Pacers")
r_patch = mpatches.Patch(color="r", label="Boston Celtics")
c_patch = mpatches.Patch(color="c", label="Toronto Raptors")
m_patch = mpatches.Patch(color="m", label="Los Angeles Lakers")
y_patch = mpatches.Patch(color="y", label="Houston Rockets")
k_patch = mpatches.Patch(color="k", label="Denver Nuggets")
tan_patch = mpatches.Patch(color="tan", label="Los Angeles Clippers")

# ______________________
# Plotting PPG

PPG_df = PPG_df.set_index(["Player"])
PPG_df = PPG_df.sort_values(["PPG"], ascending=False)

PPG_df["PPG"].plot(
    kind="bar", stacked=True, rot=90, color=map(d2c.get, PPG_df["color"])
)
plt.tight_layout()

plt.legend(
    handles=[b_patch, g_patch, r_patch, c_patch, m_patch, y_patch, k_patch, tan_patch],
    loc="upper right",
)

plt.title("NBA player statistics over PPG")
plt.savefig("NBA player statistics/players over ppg.png")
plt.show()

# ______________________
# Plotting PPG
BPG_df = BPG_df.set_index(["Player"])
BPG_df = BPG_df.sort_values(["BPG"], ascending=False)

BPG_df["BPG"].plot(
    kind="bar", stacked=True, rot=90, color=map(d2c.get, BPG_df["color"])
)
plt.tight_layout()

plt.legend(
    handles=[b_patch, g_patch, r_patch, c_patch, m_patch, y_patch, k_patch, tan_patch],
    loc="upper right",
)

plt.title("NBA player statistics over BPG")
plt.savefig("NBA player statistics/players over bpg.png")
plt.show()

# ______________________
# Plotting PPG

RPG_df = RPG_df.set_index(["Player"])
RPG_df = RPG_df.sort_values(["RPG"], ascending=False)

RPG_df["RPG"].plot(
    kind="bar", stacked=True, rot=90, color=map(d2c.get, RPG_df["color"])
)
plt.tight_layout()

plt.legend(
    handles=[b_patch, g_patch, r_patch, c_patch, m_patch, y_patch, k_patch, tan_patch],
    loc="upper right",
)

plt.title("NBA player statistics over RPG")
plt.savefig("NBA player statistics/players over rpg.png")
plt.show()
