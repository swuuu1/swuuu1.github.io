import urllib.request
from bs4 import BeautifulSoup
from time import sleep

def download_team_url(team):
    """"
    returns the basketball reference url for a given team
    """
    base_url = 'https://www.basketball-reference.com/teams/'
    
    # clean player string into url format
    team = team.upper()
    team_url = f'{team}/2023.html'

    url = base_url + team_url
    return url
# print(download_team_url('WAS'))


def download_page(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)

def parse_html(html):
    """
    Analyze the html page, find the information and return team stats as a dictionary
    """
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    
    stats_dict = {}

    team_stats_table = str(soup.find("div", attrs={"id": "all_team_and_opponent"}))
    # find fg per game
    fg_per_g = team_stats_table.split('fg_per_g" >')[1].split("<")[0]
    stats_dict['fg_per_g'] = fg_per_g
    # find ppg
    ppg = team_stats_table.split('pts_per_g" >')[1].split("<")[0]
    stats_dict['pts_per_g'] = ppg

    team_misc_table = str(soup.find("div", attrs={"id": "all_team_misc"}))
    # find ortg
    ortg = team_misc_table.split('off_rtg" >')[1].split("<")[0]
    stats_dict['off_rtg'] = ortg
    # find drtg
    drtg = team_misc_table.split('def_rtg" >')[1].split("<")[0]
    stats_dict['def_rtg'] = drtg
    
    return stats_dict

def team_stat_search(team):
    """return stats for a team"""
    url = download_team_url(team)
    stats = parse_html(download_page(url).read())
    return stats

def all_team_stat_search():
    """return a stat_dict for each team in the NBA"""
    # How to perform this without submitting a request every time?
    teams_list = ['ATL', 'BOS', 'BRK', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']
    team_stats_dict = {}

    for team in teams_list:
        print(team)
        url = download_team_url(team)
        # print(url)
        stats = parse_html(download_page(url).read())
        team_stats_dict[team] = stats
        sleep(1)
    return team_stats_dict

def main():
    team = 'WAS'
    stats = all_team_stat_search()

    print(stats)

if __name__ == "__main__":
    main()