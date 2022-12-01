import pandas as pd
from operator import add
import numpy as np
import pickle

df = pd.read_csv('data_21.csv',skipinitialspace=True)
team_stat={}
team_stat_away={}
team_stat_count={}
team_stat_away_count={}

for i in range(len(df.iloc[:,12])):
    if (df.iloc[i,12] == "A"):
        df.iloc[i,12] = -1
    elif (df.iloc[i,12] == "H"):
        df.iloc[i,12] = 1
    else:
        df.iloc[i,12] = 0

for i in range(0,len(df)):
    if(df.iloc[i,0] in team_stat):
        team_stat[df.iloc[i,0]] = list(map(add, team_stat[df.iloc[i,0]], df.iloc[i,2:12]))
        team_stat_count[df.iloc[i,0]] =  team_stat_count[df.iloc[i,0]]+1 
    else:
       team_stat[df.iloc[i,0]] =df.iloc[i,2:12]
       team_stat_count[df.iloc[i,0]] = 1

for i in range(0,len(df)):
    if(df.iloc[i,1] in team_stat_away):
        team_stat_away[df.iloc[i,1]] = list(map(add, team_stat_away[df.iloc[i,1]], df.iloc[i,2:12])) 
        team_stat_away_count[df.iloc[i,1]] = team_stat_away_count[df.iloc[i,1]] + 1
    else:
       team_stat_away[df.iloc[i,1]] =df.iloc[i,2:12]
       team_stat_away_count[df.iloc[i,1]] = 1

final_stat={}
for i in range(0,len(df)):
    home_team = df.iloc[i,0]
    away_team = df.iloc[i,1]
    final_stat[home_team+"_"+away_team] = team_stat[home_team] + team_stat_away[away_team]

df2 = pd.read_csv('data_22.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTR'])
input=[]
output=[]
for i in range(0,len(df2)):
    key = df2.iloc[i,:].HomeTeam+"_"+df2.iloc[i,:].AwayTeam
    if key in final_stat:
        if (df2.iloc[i,:].FTR == "A"):
            df2.iloc[i,:].FTR = -1
        elif (df2.iloc[i,:].FTR == "H"):
            df2.iloc[i,:].FTR = 1
        else:
            df2.iloc[i,:].FTR = 0
        input.append(final_stat[key])
        output.append(df2.iloc[i,:].FTR)


filename = "my_model"
with open(filename,'rb') as file:
    aam_acchar = pickle.load(file)

#output = aam_acchar.predict(input)

score = (aam_acchar.score(input,output))

print(output)