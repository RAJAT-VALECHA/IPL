import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# To remove un-necessary warnings
import warnings
warnings.filterwarnings("ignore")
deliveries = pd.read_csv('C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\IPL Ball-by-Ball 2008-2020.csv')
matches = pd.read_csv('C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\IPL Matches 2008-2020.csv')
def Bating_Score(name):
    try:
        Batsman_Group = deliveries.groupby(['batsman'])
        Batsman = pd.DataFrame(Batsman_Group['ball'].count()).rename(columns={'ball':'balls_faced'})
        Batsman['innings'] = Batsman_Group['id'].nunique()
        Batsman['runs'] = Batsman_Group['batsman_runs'].sum()
        Batsman['4s'] = deliveries[deliveries['batsman_runs'] == 4].groupby('batsman')['batsman_runs'].count()
        Batsman['4s'].fillna(0,inplace=True)
        Batsman['6s'] = deliveries[deliveries['batsman_runs'] == 6].groupby('batsman')['batsman_runs'].count()
        Batsman['6s'].fillna(0,inplace=True)

        # Batting average = total rus scored/no. of times batsman is been dismissed
        # Approximated here to matches instead of no. of dismissals
        Batsman['bat_average'] = round(Batsman['runs']/Batsman['innings'],2)
        avg_avg = round(Batsman['bat_average'].sum()/Batsman['bat_average'].count(),2)
        # Strike Rate = (Runs Scored / Balls faced) * 100
        Batsman['bat_strike'] = round(Batsman['runs']/Batsman['balls_faced']*100,2)
        avg_SR = round(Batsman['bat_strike'].sum()/Batsman['bat_strike'].count(),2)
        Batsman['Score']=(round(Batsman['bat_strike']/avg_SR,2)+round(Batsman['bat_average']/avg_avg,2))*Batsman['runs']
        Batsman['Score'] = round(Batsman['Score']/Batsman['innings'],2 )
        answer = Batsman['Score'][name]
    except:
        answer = 52
    if(answer<16):
        answer=52
    return answer

def Bowling_Score(name):
    try:
        Bowler_Group = deliveries.groupby(['bowler'])

        # Create a bowling dataframe (Bowler) with a summary statistics for each batsman
        Bowler = pd.DataFrame(Bowler_Group['ball'].count()).rename(columns={'ball':'balls_bowled'})

        # No. of Innings
        Bowler['innings'] = Bowler_Group['id'].nunique()
        # Get no. of wickets taken by each bowler
        bwl_wkts = deliveries[deliveries['dismissal_kind'].isin(['caught','bowled', 'lbw','stumped', 'caught and bowled', 'hit wicket'])]
        Bowler['wickets'] = bwl_wkts.groupby(['bowler'])['ball'].count()
        Bowler['wickets'].fillna(0,inplace=True)
        avg_wickets = round(Bowler['wickets'].sum()/Bowler['wickets'].count(),2)

        # Calculate the total no. of overs bowled
        overs = pd.DataFrame(deliveries.groupby(['bowler','id'])['over'].nunique())
        Bowler['overs'] = overs.groupby(['bowler'])['over'].sum()


        # Calculate the runs conceded
        Bowler['runs_conceded'] = deliveries.groupby('bowler')['batsman_runs'].sum()
        Bowler['runs_conceded'] = Bowler['runs_conceded'].fillna(0)
        # Add the runs conceded through wide and noball
        Bowler['runs_conceded'] = Bowler['runs_conceded'].add(deliveries[deliveries['extras_type'].isin(['wides','noballs'])].groupby('bowler')['extra_runs'].sum(),fill_value=0)

        # Note - roughly apprx to overs.  Should be runs_conceded/overs.balls
        Bowler['bowl_econ'] = round(Bowler['runs_conceded']/Bowler['overs'],2)
        avg_econ = round(Bowler['bowl_econ'].sum()/Bowler['bowl_econ'].count(),2)
        Bowler['Score']=(round(Bowler['bowl_econ']/avg_econ,2)+round(Bowler['wickets']/avg_wickets,2))*Bowler['wickets']
        Bowler['Score'] = round(Bowler['Score']*12.5/Bowler['innings'],2 )
        answer = (Bowler["Score"][name])
    except:
        answer = 32
    if(answer<8):
        answer=32
    return answer

def Score(name):
    answer=Bowling_Score(name)+Bating_Score(name)
    return answer
