# TODO:Import flask, requests, matplotlib, datetime, & bootstrap
from flask import Flask, render_template, Response
from flask_bootstrap import Bootstrap
import requests
from matplotlib import pyplot as plt
import datetime
import pandas
import json
import numpy as np
import os
from matplotlib.figure import Figure

app = Flask(__name__)

def getCrimeData(**kwargs):
    '''    seleceted_options = []
    for stat in kwargs:
        if type(stat) is str:
            seleceted_options.append(stat)
        else:
            continue'''
    qeury_options = ["agencies"]
    url = "https://api.usa.gov/crime/fbi/sapi/api/"
    crime_key = os.environ.get("crime_key")
    param = {'api_key': crime_key
             }
    request = requests.get(url=url, params=param)
    data = request.json()
    return data



def getCrimeOris():
    data = getCrimeData()
    codes = {}
    abbr = ['AL', 'DC', 'KY', 'OH', 'AK', 'LA', 'OK', 'AZ', 'ME', 'OR', 'AR', 'MD', 'PA', 'MA', 'MI', 'RI', 'CO', 'MN',
            'CT', 'MS', 'SD', 'DE', 'MO', 'TN', 'MT', 'TX', 'FL', 'NE', 'GA', 'NV', 'UT', 'NH', 'VT', 'HI', 'NJ', 'VA',
            'ID', 'NM', 'IL', 'NY', 'WA', 'IN', 'NC', 'WV', 'IA', 'ND', 'WI', 'KS', 'WY', 'SC', 'PR', 'GM', 'VI', 'CA']
    for state in abbr:
        codes[state] = {}
    try:
        with open('ori_codes.json', 'r') as ori_codes:
            if os.path.getsize(ori_codes) == 0:
                raise FileNotFoundError
            else:
                pass
    except FileNotFoundError:
        with open('ori_codes.json', 'w') as ori_codes:
            for state_abbr in data:
                for code in data[state_abbr]:
                    codes[state_abbr].update({data[state_abbr][code]['ori']: data[state_abbr][code]['agency_name']})
            json.dump(codes, ori_codes, indent=4)


##TODO:Update data once at 6:00 AM Monday - Friday


###TODO:Have main page that can take in selected filters and output new page with aggregated data that may be specific to
### county, state, agency, type of offense, and more.
@app.route('/')
@app.route('/home')
def home():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([4, 2])
    fig.savefig("static/css/graph.png")
    return render_template('index.html', img="static/css/graph.png")


####TODO:Make a resources page for people who want to reference data sources
@app.route('/resources')
def resources():
    return render_template('resources.html')


#####TODO:Have mission page and future outlooks for more context and features for data
@app.route('/mission')
def mission():
    return render_template('mission.html')


######TODO:Create search page where visitors can create graphs with their own search criteria
@app.route('/search')
def search():
    return render_template('search.html')


#######TODO:Create search results page
@app.route('/search_results/<path:search_params>')
def searchResults(search_params):
    pass


if __name__ == "__main__":
    app.run(debug=True)
