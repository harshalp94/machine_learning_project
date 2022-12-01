import pandas as pd

team_2021 = {
}


def get_unique_team_names():
    team_list = []
    fb_co_data_list = []
    fb_ref_list = []
    for i in range(0, 7):
        df = pd.read_csv(f'fb_co_data_{0}.csv')
        team_name = df[df['HomeTeam']]


df = pd.read_csv(f'fb_co_data_0.csv')

team_name = df[df['HomeTeam']]
#team_name.dropna()
print(team_name)