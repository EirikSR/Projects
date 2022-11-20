from bs4 import BeautifulSoup
import requests as req
from requesting_urls import get


def extract_events(table):
    """Table of FIS skiing events and returnes the tables for date, event and venue

    Args:
        BeautifulSoup table: A Table created by beautifull soup

    Returns:
        List        : List with three columns, Date, Venue and Event with rows for each event
    """

    ex_table = []

    # Due to several events using the same venue, the venue needs to be stored
    venue = ""
    # Each line in the table is itterated through, and data extracted
    for items in table:
        line = items.find_all(["th", "td"])
        row = []

        # Try/catch due to some rows being empty
        try:
            if line[2].text[0:3] == "[nb":
                a = line[2].text.rsplit(" ", 1)[0]
                row.append(a[6:])
            else:
                row.append(line[2].text.rsplit(" ", 1)[0])

            if len(line) == 9:

                row.append(line[3].text[1:])

                row.append(line[4].text[0:6])
                venue = line[3].text[1:]
            elif len(line) == 8:

                row.append(venue)

                row.append(line[3].text[0:6])

        except IndexError:
            pass
        # Only complete lists are appended
        if len(row) == 3:
            ex_table.append(row)
    return ex_table


url = "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup"

data = req.get(url)

soup = BeautifulSoup(data.text, "html.parser")


soup_table = soup.find("table", class_="wikitable").find_all("tr")[1::1]

a = extract_events(soup_table)

# Structuring the output table
string = "| Date           | Venue                | Event     | Winner        |\n|----------------|----------------------|-----------|---------------|\n"
for r in a:
    # Some venues have "  " at start, this is a little quickfix
    if r[1][1] is " ":
        r[1] = r[1][2:]

    while len(r[0]) < 16:
        r[0] = r[0] + " "
    while len(r[1]) < 22:
        r[1] = r[1] + " "
    while len(r[2]) < 11:
        r[2] = r[2] + " "

    string += "|" + r[0] + "|" + r[1] + "|" + r[2] + "|" + "               |\n"


out_table = open("datetime_filter/output.md", "w", encoding="utf-8")
out_table.write(string)
out_table.close()
