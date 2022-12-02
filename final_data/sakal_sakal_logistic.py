import pandas as pd
from operator import add
import numpy as np
import pickle

df21 = pd.read_csv('data_21.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','ref_xg_home','ref_xg_away'])
df20 = pd.read_csv('data_20.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','ref_xg_home','ref_xg_away'])
df19 = pd.read_csv('data_19.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','ref_xg_home','ref_xg_away'])
df18 = pd.read_csv('data_18.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','ref_xg_home','ref_xg_away'])
df17 = pd.read_csv('data_17.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','ref_xg_home','ref_xg_away'])


doclist = [df21,df20,df19,df18,df17]

team_stat_next={}
team_stat_away_next={}


#print(df13.FTR)
train_output=[]
test_output=[]
train_input=[]
test_input=[]
count=0
output=[]
input=[]

for index in range(0,2):
    doclist[index] = doclist[index].replace(np.nan, 0)
    final_away={}
    final_home={}
#home result
    team_stat={}
    team_stat2={}
    team_stat3={}
    output_stat={}
    teams = set(doclist[index].HomeTeam)
    teams_previous = set(doclist[index+1].HomeTeam)
    teams_previous2 = set(doclist[index+2].HomeTeam)
    teams_previous3 = set(doclist[index+3].HomeTeam)

    teams_all = teams_previous.intersection(teams_previous2)
    teams_all = teams_all.intersection(teams_previous3)

    for i in range(0,len(doclist[index])):
        output_stat[doclist[index].HomeTeam[i]+"_"+doclist[index].AwayTeam[i]] =doclist[index].iloc[i,2:]
        
    for i in range(0,len(doclist[index+1])):
        team_stat[doclist[index].HomeTeam[i]+"_"+doclist[index].AwayTeam[i]] =doclist[index].iloc[i,2:]

    for i in range(0,len(doclist[index+2])):
        team_stat2[doclist[index].HomeTeam[i]+"_"+doclist[index].AwayTeam[i]] =doclist[index].iloc[i,2:]

    for i in range(0,len(doclist[index+3])):
        team_stat3[doclist[index].HomeTeam[i]+"_"+doclist[index].AwayTeam[i]] =doclist[index].iloc[i,2:]

    for i in range(0,len(doclist[index])):
        if(doclist[index].HomeTeam[i] in teams_all and doclist[index].AwayTeam[i] in teams_all):
            key = doclist[index].HomeTeam[i]+'_'+doclist[index].AwayTeam[i]
            arr= np.append(team_stat[key],team_stat2[key])
            if(index ==0):
                test_input.append(np.append(arr,team_stat3[key]))
                test_output.append(doclist[index].FTR[i])
            else:
                input.append(np.append(arr,team_stat3[key]))
                
                output.append(doclist[index].FTR[i])


from sklearn.linear_model import LogisticRegression
model = LogisticRegression(penalty='l2',max_iter=100000,multi_class="multinomial")

model.fit(input, output)
import pdb; pdb.set_trace()