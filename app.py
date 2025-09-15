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
        name = request.args['name']
        print(name)
        if name in players[0]["full_name"]:
            return f'{players[0]}'
        else:
            return '<h1>Player not found!</h1>'
    else:
        return render_template('index.html')
if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('templates/*.html')
    server.watch('static/')
    server.watch('app.py')
    server.serve(port=5555, liveport=35729)
