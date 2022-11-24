import requests
from bs4 import BeautifulSoup
import pandas as pd

fb_ref_links = [
    'https://fbref.com/en/comps/9/2021-2022/schedule/2021-2022-Premier-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/9/2021-2022/schedule/2020-2021-Premier-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/9/2021-2022/schedule/2019-2020-Premier-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/9/2021-2022/schedule/2018-2019-Premier-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/9/2021-2022/schedule/2017-2018-Premier-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/9/2021-2022/schedule/2016-2017-Premier-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/9/2021-2022/schedule/2015-2016-Premier-League-Scores-and-Fixtures',
]
# URL = "https://fbref.com/en/comps/9/2021-2022/schedule/2021-2022-Premier-League-Scores-and-Fixtures"
football_co_data = [
    'https://www.football-data.co.uk/mmz4281/2122/E0.csv',
    'https://www.football-data.co.uk/mmz4281/2021/E0.csv',
    'https://www.football-data.co.uk/mmz4281/1920/E0.csv',
    'https://www.football-data.co.uk/mmz4281/1819/E0.csv',
    'https://www.football-data.co.uk/mmz4281/1718/E0.csv',
    'https://www.football-data.co.uk/mmz4281/1617/E0.csv',
    'https://www.football-data.co.uk/mmz4281/1516/E0.csv',

]

def get_fb_ref_data(url_list):
    for url in url_list:
        df = pd.read_html(url)
        df.to_csv('')

#page = requests.get(URL)
#df = pd.read_csv(url_2)
# print(page)
# soup = BeautifulSoup(page.content, "html.parser")
# res = soup.find(id='div_sched_2021-2022_9_1')

# df = pd.read_html(url_2)[0]
df = pd.read_html('https://fbref.com/en/comps/9/2021-2022/schedule/2021-2022-Premier-League-Scores-and-Fixtures')[0]
print(df)
#print(df.to_string())
