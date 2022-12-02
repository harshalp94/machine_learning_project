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

for index in range(0,len(doclist)):
    doclist[index] = doclist[index].replace(np.nan, 0)
    final_away={}
    final_home={}
#home result
    team_stat={}
    team_stat_count={}
    
    for i in range(0,len(doclist[index])):
        if(doclist[index].HomeTeam[i] in team_stat):
            team_stat[doclist[index].HomeTeam[i]] = list(map(add, team_stat[doclist[index].HomeTeam[i]], doclist[index].iloc[i,2:]))
            team_stat_count[doclist[index].HomeTeam[i]] =  team_stat_count[doclist[index].HomeTeam[i]]+1 
        else:
            team_stat[doclist[index].HomeTeam[i]] =doclist[index].iloc[i,2:]
            team_stat_count[doclist[index].HomeTeam[i]] = 1
    if (index != 0):
        for key in team_stat:
            if (key in team_stat_next):
                final_home[key] =np.append( team_stat[key],team_stat_next[key][11:])
    team_stat_next = team_stat

#away result
    team_stat_away={}
    team_stat_away_count={}

    
    for i in range(0,len(doclist[index])):
        if(doclist[index].AwayTeam[i] in team_stat_away):
            team_stat_away[doclist[index].AwayTeam[i]] = list(map(add, team_stat_away[doclist[index].AwayTeam[i]], doclist[index].iloc[i,2:]))
            team_stat_away_count[doclist[index].AwayTeam[i]] =  team_stat_away_count[doclist[index].AwayTeam[i]]+1 
        else:
            team_stat_away[doclist[index].AwayTeam[i]] =doclist[index].iloc[i,2:]
            team_stat_away_count[doclist[index].AwayTeam[i]] = 1
    if (index != 0):
        for key in team_stat_away:
            if (key in team_stat_away_next):
                final_away[key] =np.append( team_stat_away[key],team_stat_away_next[key][11:])
    team_stat_away_next = team_stat_away

    final_stat={}

    for i in range(0,len(doclist[index])):
        home_team = doclist[index].HomeTeam[i]
        away_team = doclist[index].AwayTeam[i]
        try:
            final_stat[home_team+"_"+away_team] = final_home[home_team] + final_away[away_team]
        except:
            continue
            
    if(index!=0):
        for i in range(0,len(doclist[index-1])):
            
            try:
                key = doclist[index-1].HomeTeam[i]+"_"+doclist[index-1].AwayTeam[i]
            except:
                continue
            if key in final_stat:
                if(index == 1):
                    count=count+1
                    test_input.append(final_stat[key])
                    test_output.append(doclist[index-1].FTR[i])
                else:
                    train_input.append(final_stat[key])
                    train_output.append(doclist[index-1].FTR[i])


from sklearn.linear_model import LogisticRegression
model = LogisticRegression(penalty='l2',max_iter=100000,multi_class="multinomial")

model.fit(train_input, train_output)
from sklearn.dummy import DummyClassifier
dummy_clf = DummyClassifier(strategy="most_frequent")
dummy_clf.fit(train_input, train_output)
import pdb; pdb.set_trace()


