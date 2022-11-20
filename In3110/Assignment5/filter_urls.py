"""
Function ran on:
• https://en.wikipedia.org/wiki/Studio_Ghibli
• https://en.wikipedia.org/wiki/Star_Wars
• https://en.wikipedia.org/wiki/Dungeons_%26_Dragons
• https://en.wikipedia.org/w/index.php
    -With separate parameters, two sets:
        *Main PAge
        *Hurricane Gonzalo
"""
# import the modules
import requests as req
import re
from requesting_urls import get


def find_urls(regex, output=None):
    """Takes a string of a regex object or string containing html code, extracts all urls found in the article and

    Args:
        regex (obj)/(str): A String consisting of html code (from a wikipedia article) or a regex object containing a string of html
        Output(str)      : (Optional) Of passed, saved all urls to a file with name $output
    Writes:
        list            : (Optional) Is output variable is passed, list will be written
    Returns:
        list             : List of the all urls found in article without duplicates
    """
    r = regex
    # Determines wether a string or object is passed, creates a list of possible urls
    if type(r) == str:

        pat = r"(?<=href\=\").+?(?=\"|\#|\ t)"
        urls = re.findall(
            pat,
            r,
        )
    else:
        pat = r"(?<=href\=\").+?(?=\"|\#|\ t)"
        urls = re.findall(
            pat,
            r.text,
        )

    # Reject urls were used for toubleshooting and locating missed formats
    lst = []
    reject = []

    # For each url, tries to reconstruct links bu comparing, then appending to string. Then appenging fixed link to output list. If not reconstructable, added to rejects
    for u in urls:

        if u[0:5] == "/wiki":
            u = "https://en.wikipedia.org" + u
            # Partitioning the url is done in two steps due to http: and https: both containing :
            head, sep, tail = u.partition(":")
            head2, sep2, tail = tail.partition(":")
            string = head + sep + head2
            lst.append(string)

        elif u[0:4] == "http":
            head, sep, tail = u.partition(":")
            head2, sep2, tail = tail.partition(":")
            string = head + sep + head2
            lst.append(string)

        elif u[0:2] == "//":
            u = "https:" + u
            head, sep, tail = u.partition(":")
            head2, sep2, tail = tail.partition(":")
            string = head + sep + head2
            lst.append(string)

        else:
            reject.append(u)

    urls = list(dict.fromkeys(lst))

    # Writes links to text is output string is passed
    if output != None:
        with open(output, "w") as f:
            for x in urls:
                f.write(x + "\n")
        f.close()

    return urls


def find_articles(urls, output=None):
    """Takes a list of urls (preferably, not necessarily) found in a wikipedia article, returns all other wikipedia articles found in list.

    Args:
        url (str)       : Url leading to wikipedia article
        Output(str)     : (Optional) Of passed, saved all urls to a file with name $output
    Writes:
        list            : (Optional) Is output variable is passed, list will be written
    Returns:
        list            : List of the all urls found in article linking to wikipedia articles
    """
    # Finds all items in list containing specified string
    print(urls)
    r = re.compile(".*wikipedia.org/w")
    new_list = list(filter(r.match, urls))
    print(new_list)

    # Writes to file if output string is passed
    if output != None:
        with open(output, "w", encoding="utf-8") as f:
            for x in new_list:
                f.write(x + "\n")
        f.close()

    return new_list


if __name__ == "__main__":
    sites = [
        "https://en.wikipedia.org/wiki/Nobel_Prize",
        "https://en.wikipedia.org/wiki/Bundesliga",
        "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup",
    ]
    output = [
        "filter_urls/Nobel_price.txt",
        "filter_urls/Bundesliga.txt",
        "filter_urls/FIS_Alpine_skiWC.txt",
    ]

    for x, y in zip(sites, output):
        pass
    r = get(sites[0])
    urls = find_urls(r)
    b = find_articles(urls, "test.txt")
