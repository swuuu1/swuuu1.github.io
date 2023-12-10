from flask import Flask, render_template, request
from player_value_calc import player_comparison  # Import your actual functions and data
from data import all_team_stats, league_stats, highest_papp  # Import your actual data

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])

def compare():
    if request.method == 'POST':
        player1 = request.form['player1']
        player2 = request.form['player2']

        p1_value, p2_value, p1, p2 = player_comparison(player1, player2)
        p1_value, p2_value = round(p1_value, 1), round(p2_value, 1)
        return render_template('result.html', p1_name=p1, p1_value=p1_value, p2_name=p2, p2_value=p2_value)

if __name__ == '__main__':
    app.run(debug=True)
