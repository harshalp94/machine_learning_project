import pandas as pd
from operator import add
import numpy as np
import pickle

df22 = pd.read_csv('data_22.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA'])
df21 = pd.read_csv('data_21.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA'])
df20 = pd.read_csv('data_20.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA'])
df19 = pd.read_csv('data_19.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA'])
df18 = pd.read_csv('data_18.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA'])
df17 = pd.read_csv('data_17.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA'])
df16 = pd.read_csv('data_16.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA'])
df15 = pd.read_csv('data_15.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA'])
df14 = pd.read_csv('data_14.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA'])
df13 = pd.read_csv('data_13.csv',skipinitialspace=True,usecols=['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HR','AR','FTR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA'])


doclist = [df21,df20,df19,df18,df17,df16,df15,df14,df13]

train_output=[]
test_output=[]
train_input=[]
test_input=[]
count=0

for index in range(0,len(doclist)):
    for i in range(0,len(doclist[index])):
        if (doclist[index].FTR[i] == "A"):
            doclist[index].FTR[i] = -1
        elif (doclist[index].FTR[i] == "H"):
            doclist[index].FTR[i] = 1
        else:
            doclist[index].FTR[i] = 0
        

for index in range(0,len(doclist)-3):

    doclist[index] = doclist[index].replace(np.nan, 0)
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
        
        try:
            team_stat[doclist[index+1].HomeTeam[i]+"_"+doclist[index+1].AwayTeam[i]] =doclist[index+1].iloc[i,2:]
        except:
            continue

    for i in range(0,len(doclist[index+2])):
        try:
            team_stat2[doclist[index+2].HomeTeam[i]+"_"+doclist[index+2].AwayTeam[i]] =doclist[index+2].iloc[i,2:]
        except:
            continue
    for i in range(0,len(doclist[index+3])):
        try:
            team_stat3[doclist[index+3].HomeTeam[i]+"_"+doclist[index+3].AwayTeam[i]] =doclist[index+3].iloc[i,2:]
        except:
            continue
    print("index:")
    for i in range(0,len(doclist[index])):

        if(doclist[index].HomeTeam[i] in teams_all and doclist[index].AwayTeam[i] in teams_all):
            key = doclist[index].HomeTeam[i]+'_'+doclist[index].AwayTeam[i]
            arr= np.append(team_stat[key],team_stat2[key])
            if(index ==0):
                test_input.append(np.append(arr,team_stat3[key]))
                test_output.append(doclist[index].FTR[i])
            else:
                train_input.append(np.append(arr,team_stat3[key]))
                
                train_output.append(doclist[index].FTR[i])


from sklearn.linear_model import LogisticRegression
model = LogisticRegression(penalty='l2',max_iter=100000,multi_class="multinomial")

import pdb; pdb.set_trace()
model.fit(train_input, train_output)
