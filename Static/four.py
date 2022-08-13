import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Plotly to create interactive graph
import chart_studio.plotly as py
from plotly import tools
from plotly.offline import init_notebook_mode,iplot
import plotly.figure_factory as ff
import plotly.graph_objs as go

def main0():
    sns.set_style("whitegrid")
    plt.style.use("fivethirtyeight")

    # To remove un-necessary warnings
    import warnings
    warnings.filterwarnings("ignore")

    deliveries = pd.read_csv('C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\IPL Ball-by-Ball 2008-2020.csv')
    matches = pd.read_csv('C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\IPL Matches 2008-2020.csv')

    x=['Sunrisers Hyderabad', 'Mumbai Indians', 'Gujarat Lions',
        'Rising Pune Supergiant', 'Royal Challengers Bangalore',
        'Kolkata Knight Riders', 'Delhi Daredevils', 'Kings XI Punjab',
        'Chennai Super Kings', 'Rajasthan Royals', 'Deccan Chargers',
        'Kochi Tuskers Kerala', 'Pune Warriors', 'Rising Pune Supergiants', 'Delhi Capitals']

    y = ['SRH','MI','GL','RPS','RCB','KKR','DC','KXIP','CSK','RR','SRH','KTK','PW','RPS','DC']

    deliveries = pd.read_csv('C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\IPL Ball-by-Ball 2008-2020.csv')
    matches = pd.read_csv('C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\IPL Matches 2008-2020.csv')

    venue_matches=matches.groupby('venue').count()[['id']].sort_values(by='id',ascending=False).head()
    ser = pd.Series(venue_matches['id'])
    venue_matches=matches.groupby('venue').count()[['id']].reset_index()

    data = [{"y": venue_matches['id'],"x": venue_matches['venue'],
              "marker": {"color": "lightblue", "size": 12},
             "line": {"color": "red","width" : 2,"dash" : 'dash'},
              "mode": "markers+lines", "name": "Women", "type": "scatter"}]

    layout = {"title": "Stadiums Vs. Matches",
              "xaxis": {"title": "Matches Played", },
              "yaxis": {"title": "Stadiums"},
              "autosize":False,"width":900,"height":700,"plot_bgcolor":"rgb(245,245,245)"}

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)
main0()
