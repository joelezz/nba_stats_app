#main.py
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from flask import Flask, render_template, request

from livereload import Server, shell

app = Flask(__name__)

app.debug = True

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/player")
def player():
    if request.method == 'GET':
        all_players = []
        all_players = players._get_players()
        last_name = request.args['last_name'].lower()
        first_name = request.args['first_name'].lower()
        results= []

        for obj in all_players:
            laste_name = obj["last_name"]
            firste_name = obj["first_name"]
            player_idd = obj["id"]

            if last_name == laste_name.lower() or first_name == firste_name.lower():
                results.append(obj)
                career = playercareerstats.PlayerCareerStats(player_id=player_idd)
                career_dict = career.get_dict()
                print(career_dict.keys())
                career_data = career_dict['resultSets'][0]  # the first result set
                print(career_data.keys())
                career_df = career.get_data_frames()[0]
                print(career_df[["SEASON_ID", "TEAM_ABBREVIATION", "PTS"]])



            
        return render_template('player.html', results=results)
    else:
        return render_template('index.html')
if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('templates/*.html')
    server.watch('static/')
    server.watch('app.py')
    server.serve(port=5555, liveport=35729)
