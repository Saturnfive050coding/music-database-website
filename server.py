from flask import Flask, render_template, request
import flask
from flask_cors import CORS

import spotify

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/tracks")
def tracks():
    print("tracks endpoint reached")
    recent_tracks = spotify.recent_tracks()
    return flask.jsonify(recent_tracks)

@app.route("/artist10", methods=['POST'])
def artist10():
    print("artist10 endpoint reached")
    artist = request.form["name"]
    print(artist)
    artist_tracks = spotify.artist_10(artist)
    return flask.jsonify(artist_tracks)


if __name__ == "__main__":
    app.run("localhost", 8000)