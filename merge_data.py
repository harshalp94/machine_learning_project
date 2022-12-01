import pandas as pd
import os
from team_names import team_name_dict

def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdirs(dir_name)

create_dir('final_data')

def get_csv(csv_name):
    df = pd.read_csv(csv_name)
    return df


def join_csv(df1, df2):
    mrg_df = df1.merge(df2, on=['HomeTeam', 'AwayTeam'], how='inner')
    return mrg_df


# Date,Time,Home,xG,Score,xG.1,Away,Attendance,Venue,Referee,Match Report,Notes,Time,Home,xG,Score,xG.1,Away,Attendance,Venue,Referee,Match Report,Notes
column_dict_ref = {
    'Unnamed': 'ref_index',
    'Time': 'ref_time',
    'Wk': 'ref_wk',
    'Day': 'ref_day',
    'Date': 'ref_date',
    'Home': 'HomeTeam',
    'Away': 'AwayTeam',
    'xG': 'ref_xg_home',
    'Score': 'ref_score',
    'xG.1': 'ref_xg_away',
    'Attendance': 'ref_attendance',
    'Venue': 'ref_venue',
    'Referee': 'ref_referee',
    'Match Report': 'ref_match_report'
}


def rename_merge_csv_files(drop_list_col):
    for i in range(0, 7):
        ref_data = get_csv(f'fb_ref_data_{i}.csv')
        ref_data.rename(columns=column_dict_ref, inplace=True)
        ref_data = ref_data.replace({'HomeTeam': team_name_dict})
        ref_data = ref_data.replace({'AwayTeam': team_name_dict})
        # print(ref_data.columns)
        ref_data.drop(columns='Unnamed: 0', axis=1, inplace=True)
        # print(ref_data.columns)
        co_data = get_csv(f'fb_co_data_{i}.csv')
        co_data = co_data.replace({'HomeTeam': team_name_dict})
        co_data = co_data.replace({'AwayTeam': team_name_dict})
        co_data.drop(columns='Unnamed: 0', axis=1, inplace=True)
        final_df = join_csv(co_data, ref_data)
        print(final_df.columns)
        final_df.drop(columns=drop_list_col, axis=1, inplace=True, errors='ignore')
        final_df.to_csv(f'final_data/final_csv_{i}.csv')


def normalize_team_name():
    return ''

drop_list = [
    'Div',
    'BWH',
    'BWD',
    'BWA',
    'IWH',
    'IWD',
    'IWA', 'PSH', 'PSD', 'PSA', 'WHH', 'WHD',
    'WHA', 'VCH', 'VCD', 'VCA', 'MaxH', 'MaxD', 'MaxA', 'AvgH',
    'AvgD', 'AvgA', 'B365>2.5', 'B365<2.5', 'P>2.5', 'P<2.5',
    'Max>2.5', 'Max<2.5', 'Avg>2.5',
    'Avg<2.5', 'AHh', 'B365AHH', 'B365AHA', 'PAHH', 'PAHA',
    'MaxAHH', 'MaxAHA', 'AvgAHH', 'AvgAHA', 'B365CH',
    'B365CD', 'B365CA', 'BWCH', 'BWCD', 'BWCA', 'IWCH', 'IWCD',
    'IWCA', 'PSCH', 'PSCD', 'PSCA', 'WHCH', 'WHCD', 'WHCA', 'VCCH', 'VCCD',
    'VCCA', 'MaxCH', 'MaxCD', 'MaxCA',
    'AvgCH', 'AvgCD', 'AvgCA', 'B365C>2.5', 'B365C<2.5', 'PC>2.5',
    'PC<2.5', 'MaxC>2.5', 'MaxC<2.5', 'AvgC>2.5', 'AvgC<2.5', 'AHCh', 'B365CAHH',
    'B365CAHA', 'PCAHH', 'PCAHA', 'MaxCAHH', 'MaxCAHA', 'AvgCAHH', 'AvgCAHA',
    'ref_referee', 'ref_match_report', 'Notes', 'ref_date', 'ref_time', 'ref_score',
    'ref_venue','ref_day', 'ref_wk', 'ref_attendance',
    'HTHG','HTAG', 'HTR', 'Referee'

]

result_dict = {
    ''
}

rename_merge_csv_files(drop_list)

# df = get_csv('final_data/final_csv_0.csv')
# print(df.to_string())


