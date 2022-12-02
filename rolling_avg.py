import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier

def rolling_averages(group, cols, new_cols, roll_match):
    group = group.sort_values("Date")
    rolling_stats = group[cols].rolling(roll_match, closed='left').mean()
    group[new_cols] = rolling_stats
    group = group.dropna(subset=new_cols)
    return group


cols = ["FTHG", "FTAG","B365H",'B365D','B365A','ref_xg_home','ref_xg_away' ]
new_cols = [f"{c}_rolling" for c in cols]

d1 = pd.read_csv(f'final_data/final_csv_0.csv')
d2 = pd.read_csv(f'final_data/final_csv_1.csv')
d_list = [d1, d2]
final_dataframe = pd.concat(d_list)
final_dataframe['Date'] = pd.to_datetime(d1['Date'])
final_dataframe['home_code'] = final_dataframe['HomeTeam'].astype('category').cat.codes
final_dataframe['away_code'] = final_dataframe['AwayTeam'].astype('category').cat.codes
final_dataframe.drop(columns=['Unnamed: 0'], axis=1, inplace=True)
final_dataframe_roll = final_dataframe.groupby('HomeTeam').apply(lambda x: rolling_averages(x, cols, new_cols,5))
final_dataframe_roll.index = range(final_dataframe_roll.shape[0])

df = pd.read_csv(f'final_df.csv')
#df = df.sort_values(['Date', 'HomeTeam'])
df_roll = df.groupby('HomeTeam').apply(lambda x: rolling_averages(x, cols, new_cols,5))
df_roll = df_roll.droplevel('HomeTeam')
df_roll.index = range(df_roll.shape[0])
print(df_roll.to_string())
encoded_col = ['home_code', 'away_code']
features = new_cols + encoded_col
target_data = ['FTR']

#model = RandomForestClassifier(n_estimators=10000, min_samples_split=100, random_state=0)
model = LogisticRegression(max_iter=100000, C=0.001, multi_class="multinomial")
#model = DummyClassifier(strategy='stratified')
print(df_roll[features].to_string())
print(df_roll['FTR'].to_string())
model.fit(df_roll[features], df_roll['FTR'])
preds = model.predict(final_dataframe_roll[features])
combined = pd.DataFrame(dict(actual=final_dataframe_roll["FTR"], predicted=preds), index=final_dataframe_roll.index)
#rf.score(d1_roll["FTR"], preds)
error = precision_score(final_dataframe_roll["FTR"], preds, average='micro')
print(combined.to_string())
print(error)