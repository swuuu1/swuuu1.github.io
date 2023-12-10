***NBA Player Comparison App***

**1. Big Idea/Goal/Why did we do this?**

Shawn and Jeffrey are both avid basketball fans, and we wanted to create something that we were passionate about. Oftentimes, we discuss basketball players, arguing about which player is better. However, we know that we have significant bias and that it would be very difficult to have an objective argument regarding the topic. Hence, we decided to create a Python application that helped settle these arguments using data and statistics. 


**2. User Instructions/README**

Install the following libraries
import urllib.request, bs4, BeautifulSoup, time, unidecode, flask


In order to run our application, go to run.py and click on the local path. 
Implementation Information
Introduction
The NBA Player Ranking Application is a web-based tool that allows users to compare and rank NBA players based on a proprietary "player score." This score is calculated using a combination of key statistics to provide users with a comprehensive assessment of player performance.
Technologies Used
Flask (Web Framework)
Python (Programming Language)
HTML, CSS (Frontend)

The user interface is designed to be intuitive, allowing users to input player statistics and receive instant rankings. The frontend is built using HTML and CSS, providing a seamless and responsive experience.

**Key Components**

*Web Scraping*

We used urllib in conjunction with BeautifulSoup to scrape the Basketball Reference website for player, team, and league statistics. 

*Flask Application*

The Flask application handles incoming requests, processes user inputs, and communicates with the player value calculation component.

*Player Value Calculation*

The player value calculation component employs a detailed algorithm to calculate a "player score" based on key statistics such as points per game, rebounds per game, and more. It also adjusts individual player statistics and places them in the context of their team. 

*Some sample code:*

    def player_comparison(player1, player2):
        """returns the values for 2 given players"""
        player1_stats = player_search.player_stat_search(player1)
        player1_team = player1_stats['team_id']
        player1_team_stats = all_team_stats[player1_team]
        team_factors = calc_team_factors(player1_team_stats, league_stats)
        player1_value = calc_player_value(team_factors, player1_stats)
        p1_name = player1_stats['name']


        player2_stats = player_search.player_stat_search(player2)
        player2_team = player2_stats['team_id']
        player2_team_stats = all_team_stats[player2_team]
        team_factors = calc_team_factors(player2_team_stats, league_stats)
        player2_value = calc_player_value(team_factors, player2_stats)
        p2_name = player2_stats['name']


        return(player1_value, player2_value, p1_name, p2_name)



**Results**


The following screenshots give an example of what our web application is capable of, specifically being able to compare two players, and providing player scores for each, allowing users to compare two players. 

![This is what our query box looks like](/images/PlayerComparison.png)

![This is what the result would look like](/images/ComparisonResult.png)

**Project Evolution/Narrative**

From the start, we wanted to create an app for comparing two NBA players. However, implementing this turned out to be a multi-step process to achieve our goal. 

The most important part of comparing two players is their stats. Lots of debates stem from personal biases towards certain players, but the one thing that is constant is stats. Basketball Reference is commonly accepted as the best public website for obtaining these stats, so our plan was to use an API that we found to retrieve the stats we needed. 

However, we had issues downloading the API, likely because it was outdated, so our only option was to create web scraping code. Once we were able to retrieve individual, team-specific, and league-wide stats, we could move on to the last step.

To finish the project, we needed to turn a website filled with hundreds of different metrics into one figure to measure player value. We researched many articles by basketball experts and analysts, and we decided on Statistical Player Value (SPV). We picked the stats we needed from the dictionaries we gathered from web scraping and put them in an algorithm to return our single number. Finally, we had accomplished our goal. 

**Attribution**

We used [this article from NBAstuffer](https://www.nbastuffer.com/analytics101/statistical-player-value-spv/#:~:text=The%20stat%20elements%20included%20in,the%20SPV%20for%20that%20game) to understand SPV. 
 
We used the following Python libraries: *urllib.request, time, BeautifulSoup, Flask, and Unidecode.*
