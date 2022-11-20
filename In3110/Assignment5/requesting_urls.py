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
# import the module
import requests as req


def get(url, params={}, output=None):
    """Takes a url ar well as optional wikipedia parameters and returnd a regex object containgin a string version of the html

    Args:
        url (str)       : A String of a wikipedia url
        params (str)    : (Optional) Wikipedia parameters, will change regex output
        output (str)    : (Optional) If passed, the html is saved to a file with $output as name

    Writes:
        html            :(Optional) Writes string from regex object to file if filname is passed

    Returns:
        regex object(obj): A regex object containing the html code as a string
    """
    r = req.get(url, params=params)

    if output != None:
        HTML_file = open(output, "w", encoding="utf-8")
        HTML_file.write("<!-- " + r.url + "--> \n")
        HTML_file.write(r.text)
        HTML_file.close()

    # print(r.url)
    return r


if __name__ == "__main__":
    # Initiating some variables
    url = "https://en.wikipedia.org/wiki/Dungeons_%26_Dragons"
    output = "Dungeons_and_Dragons.html"

    title = "Hurricane_Gonzalo"

    # Params have to be uncommented to be ran
    params = {}  # "title": title, "oldid": "983056166", "action": "info",}

    r = get(url, params, output)