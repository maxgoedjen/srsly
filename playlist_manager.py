import os
import threading

from spotify import ArtistBrowser, Link, ToplistBrowser, SpotifyError, Track
from spotify.manager import (SpotifySessionManager, SpotifyContainerManager)

PLAYLIST_NAME = 'Sirius XM'
PLAYLIST_MAX_LENGTH = 100

class PlaylistManager(SpotifySessionManager):

	appkey_file = os.path.join(os.path.dirname(__file__), 'spotify_appkey.key')
	
	def connect(self):
		download_thread = threading.Thread(target=SpotifySessionManager.connect, args=[self])
		download_thread.start()
		
	def logged_in(self, session, error):
		if error:
			print error
			return
		print "Logged in!"
		self.playlist_container = session.playlist_container()

	def add_to_playlist(self, track):
		playlist = self.playlist()
		if not playlist or track.name() not in [x.name() for x in list(playlist)[-5:]]:
			print 'Adding %s - %s' % (track.name(), track.artists()[0].name())
			playlist.add_tracks(len(playlist), [track])
		self.trim_playlist(playlist)
			
	def playlist(self):
		for x in self.playlist_container:
			if x.name() == PLAYLIST_NAME:
				return x
			
		print 'Playlist does not exist, creating playlist "%s"' % PLAYLIST_NAME
		return self.playlist_container.add_new_playlist(PLAYLIST_NAME)

		
	def trim_playlist(self, playlist):
		pass
		
	def add_track_for_query(self, query):
		def search_handler(results, userinfo):
			if results and results.tracks():
				self.add_to_playlist(results.tracks()[0])
			else:
				print 'Unable to find track: %s' % query
		self.session.search(query, search_handler)