import pandas as pd

team_2021 = {
}


def get_unique_team_names():
    team_set = set()
    fb_co_data_list = []
    fb_ref_list = []
    for i in range(0, 7):
        df = pd.read_csv(f'fb_co_data_{i}.csv')
        df = df.replace({'HomeTeam': team_name_dict})
        team_name = df['HomeTeam'].replace(r'\n',' ', regex=True).tolist()
        team_set.update(team_name)
        #print(team_name_set)
    for i in range(0,7):
        df = pd.read_csv(f'fb_ref_data_{i}.csv')
        df = df.replace({'Home': team_name_dict})
        team_name = df['Home'].replace(r'\n',' ', regex=True).tolist()
        team_set.update(team_name)

    #team_set = set(team_list)
    return team_set


team_name_dict = {
    'Leeds': 'Leeds United',
    'Leeds United': 'Leeds United',
    'Norwich City': 'Norwich City',
    'Norwich': 'Norwich City',
    'Man City': 'Manchester City',
    'Man United': 'Manchester United',
    'Manchester Utd': 'Manchester United',
    'Manchester City': 'Manchester City',
    'Sheffield': 'Sheffield United',
    'Sheffield Utd': 'Sheffield United',
    'Newcastle Utd': 'Newcastle United',
    'Newcastle': 'Newcastle United',
    'Hull': 'Hull City',
    'Hull City': 'Hull City',
    'Stoke': 'Stoke City',
    'Stoke City': 'Stoke City',
    'Swansea': 'Swansea City',
    'Swansea City': 'Swansea City',
    'Leicester': 'Leicester City',
    'Leicester City': 'Leicester City',
    'Cardiff': 'Cardiff City',
    'Cardiff City': 'Cardiff City',
}

print(get_unique_team_names())
print(len(get_unique_team_names()))

# df = pd.read_csv(f'fb_co_data_0.csv')
# df1 = pd.read_csv(f'fb_ref_data_0.csv')
# #team_name = df['HomeTeam'].replace(r'\n',' ', regex=True)
# team_name_norm = df.replace({'HomeTeam': team_name_dict})
# team_ref_norm = df1.replace({'Home': team_name_dict})
# print(team_ref_norm['Home'])
# print(team_name_norm['HomeTeam'])
