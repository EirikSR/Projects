# IN3110-eiriksro
## README eiriksro Assignment5



#### Requirements (specified in setup.py)
altair==4.1.0
attrs==20.3.0
click==7.1.2
entrypoints==0.3
Flask==1.1.2
importlib-metadata==3.1.0
itsdangerous==1.1.0
Jinja2==2.11.2
jsonschema==3.2.0
MarkupSafe==1.1.1
numpy==1.19.4
pandas==1.1.4
pyrsistent==0.17.3
python-dateutil==2.8.1
pytz==2020.4
six==1.15.0
toolz==0.11.1
Werkzeug==1.0.1
zipp==3.4.0


#### Files
- web_visualization.py
- /templates/index.html
- output.json


#### PLOT METHODS
- plot_cumulative_cases()
    Takes a string consisting of the name of a Norwegian county, as well as optional start and end dates.
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
    
- plot_reported_cases()
    Takes a string consisting of the name of a Norwegian county, as well as optional start and end dates.
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
    
- plot_both()
    Takes a string consisting of the name of a Norwegian county, as well as optional start and end dates.
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
    

- plot_norway()
    Takes no arguments. Reads file from /covid_data consisting of last weeks (spanning 19/11/2020 - 26/11/2020) and created a interactive
    map of norway. The data consists of cases per 100k inhabitants, the map is hoverable to obtain further information on a county to county basis.

    Reads:
        /covid_data/[filename].cvs
                        : A folder in this directory holds the table to be read
    Returns:
        Graph(obj)      : Altair object of the produced graph (map of norway with covid data incorporated)
    Writes:
        output.json     : A Json file of the produced plot, to be used in web app

#### Flask Methods
- index()
    Initiates the web page, displays the index.html
- plot()
    Upon refresh, plots the json named "output.json" in work directory
- action()
    Upon chosing element from dropdown menu, this function is ran, taking thedropdown argument and creating a corresponding plot for selected county


#### Useage

Examples:
``` python
>>> python web_visualization.py
```
Web app is run from directory /IN3110-EIRIKSRO/Assignment6/web_visualization.py
