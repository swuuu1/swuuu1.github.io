league_stats = {'fg_per_g': '42.0', 'pts_per_g': '114.7'}
all_team_stats = {
    "ATL": {
        "fg_per_g": "44.6",
        "pts_per_g": "118.4",
        "off_rtg": "116.6",
        "def_rtg": "116.3",
    },
    "BOS": {
        "fg_per_g": "42.2",
        "pts_per_g": "117.9",
        "off_rtg": "118.0",
        "def_rtg": "111.5",
    },
    "BRK": {
        "fg_per_g": "41.5",
        "pts_per_g": "113.4",
        "off_rtg": "115.0",
        "def_rtg": "114.1",
    },
    "CHO": {
        "fg_per_g": "41.3",
        "pts_per_g": "111.0",
        "off_rtg": "109.2",
        "def_rtg": "115.3",
    },
    "CHI": {
        "fg_per_g": "42.5",
        "pts_per_g": "113.1",
        "off_rtg": "113.5",
        "def_rtg": "112.2",
    },
    "CLE": {
        "fg_per_g": "41.6",
        "pts_per_g": "112.3",
        "off_rtg": "116.1",
        "def_rtg": "110.6",
    },
    "DAL": {
        "fg_per_g": "40.0",
        "pts_per_g": "114.2",
        "off_rtg": "116.8",
        "def_rtg": "116.7",
    },
    "DEN": {
        "fg_per_g": "43.6",
        "pts_per_g": "115.8",
        "off_rtg": "117.6",
        "def_rtg": "114.2",
    },
    "DET": {
        "fg_per_g": "39.6",
        "pts_per_g": "110.3",
        "off_rtg": "110.7",
        "def_rtg": "118.9",
    },
    "GSW": {
        "fg_per_g": "43.1",
        "pts_per_g": "118.9",
        "off_rtg": "116.1",
        "def_rtg": "114.4",
    },
    "HOU": {
        "fg_per_g": "40.6",
        "pts_per_g": "110.7",
        "off_rtg": "111.4",
        "def_rtg": "119.3",
    },
    "IND": {
        "fg_per_g": "42.0",
        "pts_per_g": "116.3",
        "off_rtg": "114.6",
        "def_rtg": "117.7",
    },
    "LAC": {
        "fg_per_g": "41.1",
        "pts_per_g": "113.6",
        "off_rtg": "115.0",
        "def_rtg": "114.5",
    },
    "LAL": {
        "fg_per_g": "42.9",
        "pts_per_g": "117.2",
        "off_rtg": "114.5",
        "def_rtg": "113.9",
    },
    "MEM": {
        "fg_per_g": "43.7",
        "pts_per_g": "116.9",
        "off_rtg": "115.1",
        "def_rtg": "111.2",
    },
    "MIA": {
        "fg_per_g": "39.2",
        "pts_per_g": "109.5",
        "off_rtg": "113.0",
        "def_rtg": "113.3",
    },
    "MIL": {
        "fg_per_g": "42.7",
        "pts_per_g": "116.9",
        "off_rtg": "115.4",
        "def_rtg": "111.9",
    },
    "MIN": {
        "fg_per_g": "42.9",
        "pts_per_g": "115.8",
        "off_rtg": "113.7",
        "def_rtg": "113.8",
    },
    "NOP": {
        "fg_per_g": "42.0",
        "pts_per_g": "114.4",
        "off_rtg": "114.4",
        "def_rtg": "112.5",
    },
    "NYK": {
        "fg_per_g": "42.0",
        "pts_per_g": "116.0",
        "off_rtg": "117.8",
        "def_rtg": "114.8",
    },
    "OKC": {
        "fg_per_g": "43.1",
        "pts_per_g": "117.5",
        "off_rtg": "115.2",
        "def_rtg": "114.2",
    },
    "ORL": {
        "fg_per_g": "40.5",
        "pts_per_g": "111.4",
        "off_rtg": "111.6",
        "def_rtg": "114.2",
    },
    "PHI": {
        "fg_per_g": "40.8",
        "pts_per_g": "115.2",
        "off_rtg": "117.7",
        "def_rtg": "113.3",
    },
    "PHO": {
        "fg_per_g": "42.1",
        "pts_per_g": "113.6",
        "off_rtg": "115.1",
        "def_rtg": "113.0",
    },
    "POR": {
        "fg_per_g": "40.5",
        "pts_per_g": "113.4",
        "off_rtg": "114.8",
        "def_rtg": "118.8",
    },
    "SAC": {
        "fg_per_g": "43.6",
        "pts_per_g": "120.7",
        "off_rtg": "119.4",
        "def_rtg": "116.8",
    },
    "SAS": {
        "fg_per_g": "43.1",
        "pts_per_g": "113.0",
        "off_rtg": "110.2",
        "def_rtg": "120.0",
    },
    "TOR": {
        "fg_per_g": "41.9",
        "pts_per_g": "112.9",
        "off_rtg": "115.5",
        "def_rtg": "114.0",
    },
    "UTA": {
        "fg_per_g": "42.5",
        "pts_per_g": "117.1",
        "off_rtg": "115.8",
        "def_rtg": "116.7",
    },
    "WAS": {
        "fg_per_g": "42.1",
        "pts_per_g": "113.2",
        "off_rtg": "114.4",
        "def_rtg": "115.6",
    },
}

# calc highest papp in the league
max_drtg = 0
for team in all_team_stats:
    def_rtg = float(all_team_stats[team]['def_rtg'])
    if def_rtg > max_drtg:
        max_drtg = def_rtg
        max_team = team

# print(max_drtg, max_team)
highest_papp = max_drtg/100