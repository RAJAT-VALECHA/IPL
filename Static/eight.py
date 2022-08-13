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
    high_scores=deliveries.groupby(['id', 'inning','batting_team','bowling_team'])['total_runs'].sum().reset_index()
    high_scores=high_scores[high_scores['total_runs']>=200]
    hss = high_scores.nlargest(10,'total_runs')

    trace = go.Table(
    header=dict(values=["Inning","Batting Team","Bowling Team", "Total Runs"],
                fill = dict(color = 'red'),
                font = dict(color = 'white', size = 14),
                align = ['center'],
               height = 30),
    cells=dict(values=[hss['inning'], hss['batting_team'], hss['bowling_team'], hss['total_runs']],
               fill = dict(color = ['lightsalmon', 'rgb(245, 245, 249)']),
               align = ['center'], font_size=13))

    layout = dict(
    width=830,
    height=410,
    autosize=False,
    title='Highest scores of IPL',
    showlegend=False,
    )

    fig1 = dict(data=[trace], layout=layout)
    iplot(fig1)

main0()
