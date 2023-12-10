import urllib.request
from bs4 import BeautifulSoup
from time import sleep
from unidecode import unidecode

def download_player_url(player, playerindex):
    """"
    returns the basketball reference url for a given player and an index(01, 02, etc.)
    """
    base_url = 'https://www.basketball-reference.com/players/'
    
    # clean player string into url format
    player = player.lower().split()
    player[0] = player[0][0:2]
    player[1] = player[1][0:5]
    player_url = f'{player[1][0]}/{player[1]}{player[0]}{playerindex}.html'

    url = base_url + player_url
    return url
# print(download_player_url('Zach Lavine', '01'))


def download_page(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)

def parse_html(html, player):
    """
    Analyze the html page, find the information and return player stats from the 2022-23 season as a dictionary
    """
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())

    # find player name
    player_info = soup.find("div", attrs={"id": "info", "class": "players"})
    # print(player_info)
    player_name = str(player_info.find("h1"))
    # print(player_name)
    # clean player name
    name = player_name.split(">")[2].split("<")[0]
    # print(name)
    
    # double-check that returned name matches searched name
    lower_name, lower_player = unidecode(name.lower()), unidecode(player.lower())
    if lower_name != lower_player:
        # print(lower_name, lower_player)
        raise AttributeError

    player_stats_table = soup.find("table", attrs={"class": "stats_table", "id": "per_game"})

    # Stats for 2022-23 season
    player_season_stats = player_stats_table.find("tr", attrs={"id": "per_game.2023", "class": "full_table"})

    # Add each stat to dictionary
    stats_dict = {'name': name}
    for stat in player_season_stats.find_all("td"):
        stats = str(stat).split("data-stat=")[1].split(">")

        # extract the name of the stat being added
        key = stats[0].strip('"')

        # extract the number for the stat being added, different for "Team" stat
        if key == 'team_id':
            value = stats[1].split('teams/')[1].split('/')[0]
        elif len(stats) > 4:
            value = stats[2].split("<")[0]
        else:
            value = stats[1].split("<")[0]

        stats_dict[key] = value

    # remove irrelevant items
    stats_dict.pop('lg_id')

    return stats_dict

def player_stat_search(player):
    """runs through player indexes for players with the same url until it reaches desired player"""
    # How to perform this without submitting a request every time?
    index = 1
    for index in range(10):
        try: 
            index_text = f'0{index}'
            url = download_player_url(player, index_text)
            # print(url)
            stats = parse_html(download_page(url).read(), player)
            return stats
        except:
            sleep(1)

def main():
    # enter any player's full name here
    guy = input('Enter full name of player: ')
    
    stats = player_stat_search(guy)

    # url = download_player_url(guy, '01')
    # stats = parse_html(download_page(url).read(), guy)

    print(stats)

if __name__ == "__main__":
    main()