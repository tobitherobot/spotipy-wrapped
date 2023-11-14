import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# paylist_length = 400

class PlaylistController:

    def __init__(self):
        self.spotipy = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='user-library-read'))
        self.user_id = ''

    def run(self):
        # Hauptablauf des Programms
        print("Das ist der Hauptablauf des Programms.")

    def read_credentials(self):

        f = open("client.txt")

        os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8080/'
        os.environ['SPOTIPY_CLIENT_ID'] = f.readline().strip()
        os.environ['SPOTIPY_CLIENT_SECRET'] = f.readline().strip()

        print(os.environ['SPOTIPY_CLIENT_ID'])
        self.user_id = f.readline().strip()

    def create_playlist(self, name):
        playlist = self.spotify.user_playlist_create(self.user_id, name, False, False, '')

    def test():
        abs_path = os.path.dirname(__file__)
        path = os.path.join(abs_path, 'test/grouped.json')
        f = open(path, "r", encoding="utf8")
        s = f.read().replace("'", "\'")
        d = json.loads(s)

    def idk():
        uris = []
        for song in d:
            uris.append(song['spotify_uri'])

        scope = 'playlist-modify-private'
        spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        spotify.playlist_add_items(playlist['uri'], uris[:100], 0)
        spotify.playlist_add_items(playlist['uri'], uris[100:200], 100)
        spotify.playlist_add_items(playlist['uri'], uris[200:300], 200)
        spotify.playlist_add_items(playlist['uri'], uris[300:400], 300)