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

    trace = go.Table(
        header=dict(values=["Team","Total Matches","Wins"],
                    fill = dict(color='#ff96ea'),
                    font = dict(color=['rgb(45, 45, 45)'] * 5, size=14),
                    align = ['center'],
                   height = 30),
        cells=dict(values=[totm['Team'], totm['Total Matches'], totm['wins']],
                   fill = dict(color=['rgb(235, 193, 238)', 'rgba(228, 222, 249, 0.65)']),
                   align = ['center'], font_size=13, height=25))

    layout = dict(
        width=750,
        height=420,
        autosize=False,
        title='Total Matches vs Wins per team',
        margin = dict(t=100),
        showlegend=False,
    )

    fig1 = dict(data=[trace], layout=layout)
    iplot(fig1)
main0()
