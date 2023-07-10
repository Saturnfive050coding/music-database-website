from flask import Flask, render_template, request
import flask
from flask_cors import CORS

import spotify
import database
import formatting

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
    artist_tracks = spotify.artist_10_list(artist)
    database.insert_playlist(artist_tracks['id'], artist_tracks['name'], artist_tracks['tracks'])
    return flask.jsonify(f"Added top 10 tracks from artist {artist} to the database")

@app.route("/playlist", methods=['POST'])
def get_playlist():
    print("get_playlist endpoint reached")
    playlistId = request.form["id"]
    playlist = database.retrieve_playlist(playlistId)
    playlist = formatting.format_playlist(playlist)
    return flask.jsonify(playlist)

@app.route("/delete", methods=["POST"])
def delete_playlist():
    print("delete_playlist endpoint reached")
    playlistId = request.form["id"]
    result = database.delete_playlist(playlistId)
    return flask.jsonify(result)

@app.route("/lists")
def search_playlists():
    print("search playlists endpoint reached")
    lists = database.read_table()
    return flask.jsonify(lists)


if __name__ == "__main__":
    app.run("localhost", 8000)