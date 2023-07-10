import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

from database import playlist_count

scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))


def recent_tracks():
    tracks = ""
    results = sp.current_user_recently_played()
    for idx, item in enumerate(results['items']):
        track = item['track']
        tracks += f"{idx} {track['artists'][0]['name']}  -  {track['name']}<br>"
        if(idx == 20):
            break
    return tracks

def playlists():
    playlists = sp.user_playlists('spotify')
    output = ""
    counter = 0
    for i, playlist in enumerate(playlists['items']):
        counter += 1
        output += f"{i+1+playlists['offset']} <{playlist['uri']}> {playlist['name']}\n"
        if counter == 10:
            break

    return output

def artist_pic(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        return f"{artist['images'][0]['url']}"
    else:
        return "Artist not found."

def artist_10(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    output = ""
    if len(items) > 0:
        artist = items[0]
        tracks = sp.artist_top_tracks(artist['uri'])
        output += f"{name} Top 10 Most Popular Tracks:<br>"
        for track in tracks['tracks'][:10]:
            output += f"<a href={track['external_urls']['spotify']}>{track['name']}</a><br>"
        return output
    else:
        return "Artist not found."

def artist_10_list(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    id = playlist_count() + 1
    print(id)
    output = {'id': id, 'name': f"{name} Top 10 Most Popular Tracks<br><br>", 'tracks': []}
    if len(items) > 0:
        artist = items[0]
        tracks = sp.artist_top_tracks(artist['uri'])
        for track in tracks['tracks'][:10]:
            output['tracks'].append(f"<a href={track['external_urls']['spotify']}>{track['name']}</a><br>")
        return output
    else:
        return "Artist not found."

