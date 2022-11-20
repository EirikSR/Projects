import requests as req
import datetime as dt
import re

# Task tested on:
url = [
    "https://en.wikipedia.org/wiki/Linus_Pauling",
    "https://en.wikipedia.org/wiki/Rafael_Nadal",
    "https://en.wikipedia.org/wiki/J._K._Rowling",
    "https://en.wikipedia.org/wiki/Richard_Feynman",
    "https://en.wikipedia.org/wiki/Hans_Rosling",
]
output = [
    "filter_dates_regex/Linus_Pauling_dates.txt",
    "filter_dates_regex/Rafael_Nadal_dates.txt",
    "filter_dates_regex/J._K._Rowling_dates.txt",
    "filter_dates_regex/Richard_Feynman_dates.txt",
    "filter_dates_regex/Hans_Rosling_dates.txt",
]


def get_dates(url, dayless=False, output=None):
    """Takes a url and finds all dates written in the standard wikipedia formats, sorts the dates in chronological order and retuns the list.

    Args:
        url (str)       : A String consisting of a webpage url, preferably Wikipedia for the function to perform as intended
        dayless (bool)  : Optional True/False statement, if True dates on the form (Month Year) (missing day) will be included
        output (str)    : Optional String, is supplied, the function will write the dates to a file with name same as output argument

    Writes:
        Optional List of all dates, numerated and sorted in chronological order

    Returns:
        list            : List of all dates found in chronological order on form "YYYYMMDD", with dates without day having 00 for day
    """
    data = req.get(url)

    months = [
        "Jan |Feb |Mar |Apr |May |Jun |Jul |Aug |Sep |Oct |Nov |Dec ",
        "January |February |March |April |May |June |July |August |September |October |November |December ",
        "January,|February,|March,|April,|May,|June,|July,|August,|September,|October,|November,|December,",
    ]
    # In order to replace month names to orderly strings, a map is constructed, taking month names and returning the -[number]
    # - Is added in order to differenciate montsh and dates in re.findall()
    month_map = {
        "January ": "-01 ",
        "February ": "-02 ",
        "March ": "-03 ",
        "April ": "-04 ",
        "May ": "-05 ",
        "June ": "-06 ",
        "July ": "-07 ",
        "August ": "-08 ",
        "September ": "-09 ",
        "October ": "-10 ",
        "November ": "-11 ",
        "December ": "-12 ",
        "Jan ": "-01 ",
        "Feb ": "-02 ",
        "Mar ": "-03 ",
        "Apr ": "-04 ",
        "May ": "-05 ",
        "Jun ": "-06 ",
        "Jul ": "-07 ",
        "Aug ": "-08 ",
        "Sep ": "-09 ",
        "Oct ": "-10 ",
        "Nov ": "-11 ",
        "Dec ": "-12 ",
        "January,": "-01",
        "February,": "-02",
        "March,": "-03",
        "April,": "-04",
        "May,": "-05",
        "June,": "-06",
        "July,": "-07",
        "August,": "-08",
        "September,": "-0",
        "October,": "-10",
        "November,": "-11",
        "December,": "-12",
    }

    # All montch converted to numbers
    match = re.sub(
        r"%s" % "".join(months[0]), lambda x: month_map[x.group()], data.text
    )
    match = re.sub(r"%s" % "".join(months[1]), lambda x: month_map[x.group()], match)
    match = re.sub(r"%s" % "".join(months[2]), lambda x: month_map[x.group()], match)

    # All different variations of writing dates subbed to a standard format
    match = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"Dstart \1\2\3 Dslutt ", match)
    match = re.sub(r"(\d{4}) -(\d{2}) (\d{2})", r"Dstart \1\2\3 Dslutt ", match)
    match = re.sub(r"(\d{2}) -(\d{2}) (\d{4})", r"Dstart \3\2\1 Dslutt ", match)
    match = re.sub(r"-(\d{2}) (\d{2}) (\d{4})", r"Dstart \3\1\2 Dslutt ", match)
    match = re.sub(r"-(\d{2}) (\d{2}), (\d{4})", r"Dstart \3\1\2 Dslutt ", match)

    # Pattern uses Dstart and Dslutt to find the dates, these expressions were chosen due to not being likely to occur naturally in an article
    pattern = r"(?<=Dstart )\d{8}(?= Dslutt)"

    dates = re.findall(pattern, match)

    if dayless == True:

        match = re.sub(r"-(\d{2}) (\d{4})", r"Dstart \2\1 Dslutt ", match)

        # This is a lazt fix, and the returned list will have to take precautions due to dates with 00 endings
        dates += [
            str(item) + "00"
            for item in re.findall(r"(?<=Dstart )\d{6}(?= Dslutt)", match)
        ]

    dates = [int(day) for day in dates]
    dates.sort()
    dates = list(dict.fromkeys(dates))

    # Of Filename for an output file is suplied, the list is written to a file with index number for each date
    if output != None:
        with open(output, "w") as f:
            for i in range(len(dates)):
                string = str(dates[i])

                # Special case for dates consisting only of month/year
                # Date is converted to string and split in order to write to file
                if string[-2:] == "00":
                    f.write(str(i + 1) + ") " + string[0:4] + "/" + string[4:6] + "\n")
                else:
                    f.write(
                        str(i + 1)
                        + ") "
                        + string[0:4]
                        + "/"
                        + string[4:6]
                        + "/"
                        + string[6:8]
                        + "\n"
                    )
    return dates


for x, y in zip(url, output):
    get_dates(x, True, y)