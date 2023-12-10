import player_search, retrieve_league_stats, retrieve_team_stats, data
all_team_stats, league_stats, highest_papp = data.all_team_stats, data.league_stats, data.highest_papp

def calc_team_factors(team_stats, league_stats):
    """calculates league and team factors for a given team in the 2022-23 season"""
    team_ppg = float(team_stats['pts_per_g'])
    team_fg_per = float(team_stats['fg_per_g'])
    team_ortg = float(team_stats['off_rtg'])
    team_drtg = float(team_stats['def_rtg'])
    league_ppg = float(league_stats['pts_per_g'])
    league_fg_per = float(league_stats['fg_per_g'])

    team_factors = {}
    team_factors['team_ppb'] = team_ppg/team_fg_per
    team_factors['team_pspp'] = team_ortg/100
    team_factors['team_papp'] = team_drtg/100
    team_factors['team_db'] = highest_papp - team_factors['team_papp']
    team_factors['league_ppb'] = league_ppg/league_fg_per

    return team_factors

def calc_player_value(team_factors, player_stats):
    """calculates value for a given player in the 2022-23 season"""
    mpg = float(player_stats['mp_per_g'])
    ppg = float(player_stats['pts_per_g'])
    rpg = float(player_stats['trb_per_g'])
    apg = float(player_stats['ast_per_g'])
    spg = float(player_stats['stl_per_g'])
    bpg = float(player_stats['blk_per_g'])
    tpg = float(player_stats['tov_per_g'])

    min_val = mpg
    pts_val = ppg
    reb_val = rpg * (team_factors['team_pspp'] + team_factors['team_db'])
    ast_val = apg * team_factors['team_ppb']
    stl_val = spg * (team_factors['team_pspp'] + team_factors['team_papp'])
    blk_val = bpg * team_factors['league_ppb']
    tov_val = tpg * -1 * (team_factors['team_pspp'] + team_factors['team_papp'])

    player_val = min_val + pts_val + reb_val + ast_val + stl_val + blk_val + tov_val
    return player_val

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

def main():
    player1 = input('Player 1: ')
    player2 = input('Player 2: ')
    p1_value, p2_value, p1, p2 = player_comparison(player1, player2)
    print(f"{p1}'s value is {p1_value:.1f} and {p2}'s value is {p2_value:.1f}. ")


if __name__ == "__main__":
    main()