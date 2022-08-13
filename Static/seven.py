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

    matches['season'] = matches['date'].str[-4:].astype(int)

    batsmen = matches[['id','season']].merge(deliveries, left_on = 'id', right_on = 'id', how = 'left').drop('id', axis = 1)
    season=batsmen.groupby(['season'])['total_runs'].sum().reset_index()
    Season_boundaries=batsmen.groupby("season")["batsman_runs"].agg(lambda x: (x==6).sum()).reset_index()
    fours=batsmen.groupby("season")["batsman_runs"].agg(lambda x: (x==4).sum()).reset_index()
    Season_boundaries=Season_boundaries.merge(fours,left_on='season',right_on='season',how='left')
    Season_boundaries=Season_boundaries.rename(columns={'batsman_runs_x':'6"s','batsman_runs_y':'4"s'})

    Season_boundaries['6"s'] = Season_boundaries['6"s']*6
    Season_boundaries['4"s'] = Season_boundaries['4"s']*4
    Season_boundaries['total_runs'] = season['total_runs']

    trace1 = go.Bar(
        x=Season_boundaries['season'],
        y=Season_boundaries['total_runs']-(Season_boundaries['6"s']+Season_boundaries['4"s']),
        marker = dict(line=dict(color='#000000', width=1)),
        name='Remaining runs',opacity=0.6)

    trace2 = go.Bar(
        x=Season_boundaries['season'],
        y=Season_boundaries['4"s'],
        marker = dict(line=dict(color='#000000', width=1)),
        name='Run by 4"s',opacity=0.7)

    trace3 = go.Bar(
        x=Season_boundaries['season'],
        y=Season_boundaries['6"s'],
        marker = dict(line=dict(color='#000000', width=1)),
        name='Run by 6"s',opacity=0.7)


    data = [trace1, trace2, trace3]
    layout = go.Layout(title="Run Distribution per year",barmode='stack',xaxis = dict(tickmode='linear',title="Year"),
                                        yaxis = dict(title= "Run Distribution"), plot_bgcolor='rgb(245,245,245)')

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)

main0()
