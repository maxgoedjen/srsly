#!/usr/bin/env python

from playlist_manager import *
from siriusxm_listener import *

if __name__ == '__main__':
    import optparse
    op = optparse.OptionParser(version="%prog 0.1")
    op.add_option("-u", "--username", help="Spotify username")
    op.add_option("-p", "--password", help="Spotify password")
    op.add_option("-c", "--channel", help="Sirius XM channel number")
    (options, args) = op.parse_args()
        
    playlist_manager = PlaylistManager(options.username, options.password, True)
    
    listener = SiriusXMListener(options.channel)
    listener.listen(playlist_manager.add_track_for_query)
    
    playlist_manager.connect()
