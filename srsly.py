#!/usr/bin/env python

from playlist_manager import *

if __name__ == '__main__':
    import optparse
    op = optparse.OptionParser(version="%prog 0.1")
    op.add_option("-u", "--username", help="Spotify username")
    op.add_option("-p", "--password", help="Spotify password")
    (options, args) = op.parse_args()
        
    test = PlaylistManager(options.username, options.password, True)
    test.connect()