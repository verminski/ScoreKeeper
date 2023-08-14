from flask import Flask, render_template, request, redirect

app = Flask(__name__)

players = []

@app.route('/')
def home():
    return render_template('index.html', players=players)

@app.route('/add_player', methods=['POST'])
def add_player():
    player_name = request.form['player_name']
    players.append({'name': player_name, 'points': 0})
    return redirect('/')

@app.route('/add_points', methods=['POST'])
def add_points():
    player_name = request.form['player_name']
    points = int(request.form['points'])
    for player in players:
        if player['name'] == player_name:
            player['points'] += points
            break
    return redirect('/')

@app.route('/end_game', methods=['GET', 'POST'])
def end_game():
    if not players:
        return render_template('no_players.html')
    else:
        winner = max(players, key=lambda p: p['points'])
        return render_template('end_game.html', players=players, winner=winner)

@app.route('/reset_game', methods=['POST'])
def reset_game():
    players.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
