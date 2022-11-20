import pandas as pd
from flask import *
import altair as alt
import datetime

alt.renderers.enable("mimetype")


def plot_reported_cases(county="Norway", start="29/03/2020", end="04/11/2020"):
    """Takes a string consisting of the name of a Norwegian county, as well as optional start and end dates.
        Using pandas, the daily reported cases for the selected area is organized and put into an Altair graph.
        Returnes an Altair figure object and saves a json file.

    Args:
        county (str)    : The name of a Norwegian county
        start (str)     : (Optional) String representing the start date (form (DD/MM/YYYY))
        end (str)       : (Optional) String representing the end date (form (DD/MM/YYYY))
    Reads:
        /covid_data/[filename].cvs
                        : A folder in this directory holds the tables read
    Returns:
        Graph(obj)      : Altair object of the produced graph (nex cases)
    Writes:
        output.json     : A Json file of the produced plot, to be used in web app
    """
    # Trying to parse datetime from strings containing date
    try:
        start = datetime.datetime.strptime(start, "%d/%m/%Y")
        end = datetime.datetime.strptime(end, "%d/%m/%Y")
    except:
        raise ValueError("Dates could not be converted to datetime")

    title = "Cases per day for " + county
    # Creating pandas dataframe
    file_name = "covid_data/number-of-reported-covid" + counties[county] + ".csv"
    df = pd.read_csv(file_name, sep=";")
    # Converting dates to datetime
    df["Date"] = pd.to_datetime(df["Date"], format="%d.%m.%Y")

    # Creating a mask containing dates between start and end date
    mask = (df["Date"] > start) & (df["Date"] <= end)
    df = df.loc[mask]

    # Setting Date column as index and plotting the cumulative cases
    df = df.set_index(df["Date"])

    chart = (
        alt.Chart(df, title=title)
        .mark_bar()
        .encode(x="Date:T", y="New cases:Q", tooltip=["Date", "New cases"])
    )
    chart.save("output.json")
    chart.show()


def plot_cumulative_cases(county="Norway", start="29/03/2020", end="04/11/2020"):

    """Takes a string consisting of the name of a Norwegian county, as well as optional start and end dates.
        Using pandas, the Cumulative corona cases for the selected area is organized and put into an Altair graph.
        Returnes an Altair figure object and saves a json file.

    Args:
        county (str)    : The name of a Norwegian county
        start (str)     : (Optional) String representing the start date (form (DD/MM/YYYY))
        end (str)       : (Optional) String representing the end date (form (DD/MM/YYYY))
    Reads:
        /covid_data/[filename].cvs
                        : A folder in this directory holds the tables read
    Returns:
        Graph(obj)      : Altair object of the produced graph (Cumulative cases)
    Writes:
        output.json     : A Json file of the produced plot, to be used in web app
    """

    # Trying to parse datetime from strings containing date
    try:
        start = datetime.datetime.strptime(start, "%d/%m/%Y")
        end = datetime.datetime.strptime(end, "%d/%m/%Y")
    except:
        raise ValueError("Dates could not be converted to datetime")
    title = "Cumulative cases for " + county
    # Creating pandas dataframe
    file_name = "covid_data/number-of-reported-covid" + counties[county] + ".csv"
    df = pd.read_csv(file_name, sep=";")
    # Converting dates to datetime
    df["Date"] = pd.to_datetime(df["Date"], format="%d.%m.%Y")

    # Creating a mask containing dates between start and end date
    mask = (df["Date"] > start) & (df["Date"] <= end)
    df = df.loc[mask]
    # print(df)
    # Setting Date column as index and plotting the cumulative cases
    df = df.set_index(df["Date"])

    chart = (
        alt.Chart(df, title=title)
        .mark_line()
        .encode(
            x="Date:T", y="Cumulative cases:Q", tooltip=["Date", "Cumulative cases"]
        )
    )
    chart.save("output.json")
    return chart


def plot_both(county="Norway", start="29/03/2020", end="04/11/2020"):

    """Takes a string consisting of the name of a Norwegian county, as well as optional start and end dates.
        Using pandas, the Cumulative corona cases and daily reported cases for the selected area is organized and put into an Altair graph.
        Returnes an Altair figure object and saves a json file.

    Args:
        county (str)    : The name of a Norwegian county
        start (str)     : (Optional) String representing the start date (form (DD/MM/YYYY))
        end (str)       : (Optional) String representing the end date (form (DD/MM/YYYY))
    Reads:
        /covid_data/[filename].cvs
                        : A folder in this directory holds the tables read
    Returns:
        Graph(obj)      : Altair object of the produced graph (cumulative + new cases with separate axis)
    Writes:
        output.json     : A Json file of the produced plot, to be used in web app
    """

    # Trying to parse datetime from strings containing date
    try:
        start = datetime.datetime.strptime(start, "%d/%m/%Y")
        end = datetime.datetime.strptime(end, "%d/%m/%Y")
    except:
        raise ValueError("Dates could not be converted to datetime")

    title = "Cases for " + county
    # Creating pandas dataframe
    file_name = "covid_data/number-of-reported-covid" + counties[county] + ".csv"

    df = pd.read_csv(file_name, sep=";")
    # Converting dates to datetime
    df["Date"] = pd.to_datetime(df["Date"], format="%d.%m.%Y")

    # Creating a mask containing dates between start and end date
    mask = (df["Date"] > start) & (df["Date"] <= end)
    df = df.loc[mask]

    # Setting Date column as index and plotting the cumulative cases
    df = df.set_index(df["Date"])

    # Creating chart for cumulative cases, adding tooltip for hovering
    chart1 = (
        alt.Chart(df)
        .mark_line()
        .encode(
            x="Date:T", y="Cumulative cases:Q", tooltip=["Date", "Cumulative cases"]
        )
    )
    # Creating chart for new cases, adding tooltip for hovering (not much of a challenge though)
    chart2 = (
        alt.Chart(df)
        .mark_bar(color="red")
        .encode(y="New cases:Q", x="Date:T", tooltip=["Date", "New cases"])
    )

    # Mergin the graphs, this ensures separate Y-axis, setting independant axis
    chart = alt.concat(
        (alt.layer(chart2, chart1, title=title).resolve_scale(y="independent")).encode()
    )

    # chart.show()
    chart.save("output.json")
    return chart


def plot_norway():
    """Takes no arguments. Reads file from /covid_data consisting of last weeks (spanning 19/11/2020 - 26/11/2020) and created a interactive
    map of norway. The data consists of cases per 100k inhabitants, the map is hoverable to obtain further information on a county to county basis.

    Reads:
        /covid_data/[filename].cvs
                        : A folder in this directory holds the table to be read
    Returns:
        Graph(obj)      : Altair object of the produced graph (map of norway with covid data incorporated)
    Writes:
        output.json     : A Json file of the produced plot, to be used in web app
    """

    # Obtaining dataset
    df = pd.read_csv("covid_data/antall-meldte-tilfeller.csv", sep=";")

    # Converting string numbers to float
    df["Insidens"] = df["Insidens"].str.replace(",", ".").astype(float)

    # Retrieve topo-json from external site
    counties = alt.topo_feature(
        "https://raw.githubusercontent.com/deldersveld/topojson/master/countries/norway/norway-new-counties.json",
        "Fylker",
    )

    nearest = alt.selection(
        # Obtains the county being howered over
        type="single",
        on="mouseover",
        fields=["properties.navn"],
        empty="none",
    )

    chart = (
        alt.Chart(counties)
        .mark_geoshape()
        .encode(
            tooltip=[
                alt.Tooltip("properties.navn:N", title="County"),
                alt.Tooltip("Insidens:Q", title="Cases per 100k capita"),
            ],
            # Creates color scheme based upon the insidens value, yellow to orange to red.
            color=alt.Color(
                "Insidens:Q",
                scale=alt.Scale(scheme="yelloworangered"),
                legend=alt.Legend(title="Cases per 100k capita"),
            ),
            # Creates outline around county being moused over
            stroke=alt.condition(nearest, alt.value("black"), alt.value(None)),
        )
        .transform_lookup(
            # Pairs data from county Json and dataframe to diplay data.
            lookup="properties.navn",
            from_=alt.LookupData(df, "Category", ["Insidens"]),
        )
        .properties(
            # Sets size and title for graph
            width=400,
            height=500,
            title="Cases per 100k for Norwegian counties",
        )
        .add_selection(nearest)
    )

    chart.save("output.json")
    return chart


# County dictionary, names and corresponding file endings.
counties = {
    "Norway": "",
    "Agder": "-1",
    "Innlandet": "-2",
    "More og Romsdal": "-3",
    "Nordland": "-4",
    "Oslo": "-5",
    "Rogaland": "-6",
    "Troms og Finnmark": "-7",
    "Trondelag": "-8",
    "Vestfold og Telemark": "-9",
    "Vestland": "-10",
    "Viken": "-11",
}


app = Flask(__name__)


@app.route("/")
def index():
    """Initiates the page"""
    return render_template("index.html")


@app.route("/help")
def help():
    return render_template("help.html")


@app.route("/plot.json")
def plot():
    """
    When refreshed, this function reads the Json file and displayes it to the page
    """
    with open("output.json") as file:
        return file.read()


@app.route("/<id>", methods=["GET"])
def action(id):
    """Using passed agrument from url, the argumant is passed onwards to specified plot function, then page is refreshed with new plot showing.

    Args:
        id(str)         : id selected from dropdown menu, corresponds to a county or interactive map
    """

    if id != "Norway_map":
        plot_both(id)

        return render_template("index.html")
    # Interactive plot has it's own designation
    elif id == "Norway_map":
        plot_norway()

        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
