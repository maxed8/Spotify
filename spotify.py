import os
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2

playlist = input('Enter a playlist to find the unique songs: ')

username = 'maxxed8'
scope = 'user-library-read'

token = util.prompt_for_user_token(username,
                           scope,
                           client_id='b5568023f3b844b885f5961c19fe1c96',
                           client_secret='ec925c2442044bfa874420d8f9ea310d',
                           redirect_uri='http://google.com/')

spotify = spotipy.Spotify(auth=token)

def get_playlist_tracks(username,playlist_id):
	results = spotify.user_playlist_tracks(username,playlist_id)
	tracks = results['items']
	while results['next']:
		results = spotify.next(results)
		tracks.extend(results['items'])
	return tracks

if token:
	playlists = spotify.current_user_playlists()
	allSongs = []
	playlistSongs = []
	for pl in playlists['items']:
		plID = pl['uri']
		tracks = get_playlist_tracks(username, plID)
		count = 0
		for song in tracks:
			if count != 35:
				if pl['name'] != playlist:
					allSongs.append(song['track']['name'])
				else:
					playlistSongs.append(song['track']['name'])
			count += 1
		#print(str(count) + ' Songs')

uniqueSongs = []
for s in playlistSongs:
	if not(s in allSongs):
		uniqueSongs.append(s)

		
print(str(len(uniqueSongs)) + ' unique song(s) in ' + playlist + ':')
for s in uniqueSongs:
	print('- ' + str(s))

for i in playlists['items']:
	print(i['name'])

