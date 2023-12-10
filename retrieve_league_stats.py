import urllib.request
from bs4 import BeautifulSoup

def download_page(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)

def league_parse_html(html):
    """
    Analyze the html page, find the information and return league stats from the 2022-23 season as a dictionary
    """
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())

    league_stats_table = soup.find("table", attrs={"id": "stats"})
    
    stats_dict = {}

    for season in league_stats_table.find_all("tr"):
        if '2022-23' in str(season):
            for stat in season.find_all("td"):
                stats = str(stat).split("data-stat=")[1].split(">")

                # extract the name of the stat being added
                key = stats[0].strip('"')

                # extract the number for the stat being added
                value = stats[1].split("<")[0]

                # add desired stats to dict
                if key == 'fg_per_g' or key == 'pts_per_g':
                    stats_dict[key] = value
            
    return stats_dict


def retrieve_league_stats():
    """"""
    url = "https://www.basketball-reference.com/leagues/NBA_stats_per_game.html"
    league_stats = league_parse_html(download_page(url).read())

    return league_stats

def main():
    league_stats = retrieve_league_stats()
    print(league_stats)

if __name__ == "__main__":
    main()