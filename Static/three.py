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

    matches.replace(x,y,inplace = True)
    deliveries.replace(x,y,inplace = True)

    matches_played=pd.concat([matches['team1'],matches['team2']])
    matches_played=matches_played.value_counts().reset_index()
    matches_played.columns=['Team','Total Matches']
    matches_played['wins']=matches['winner'].value_counts().reset_index()['winner']

    matches_played.set_index('Team',inplace=True)
    totm = matches_played.reset_index().head(8)

    trace1 = go.Bar(x=matches_played.index,y=matches_played['Total Matches'],
                    name='Total Matches',opacity=0.4)

    trace2 = go.Bar(x=matches_played.index,y=matches_played['wins'],
                    name='Matches Won',marker=dict(color='red'),opacity=0.4)

    trace3 = go.Bar(x=matches_played.index,
                   y=(round(matches_played['wins']/matches_played['Total Matches'],3)*100),
                   name='Win Percentage',opacity=0.6,marker=dict(color='gold'))

    data = [trace1, trace2, trace3]

    layout = go.Layout(title='Match Played, Wins And Win Percentage',xaxis=dict(title='Team'),
                       yaxis=dict(title='Count'),bargap=0.2,bargroupgap=0.1, plot_bgcolor='rgb(245,245,245)')

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)
main0()
