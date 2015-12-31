# WARNING - srsly is deprecated in favor of [canis](https://github.com/maxgoedjen/canis)


# srsly

A Spotify playlist generator that adds songs as they're played on Sirius XM.

## Setup

You're gonna need a Spotify dev key. You can get one [here](https://developer.spotify.com/technologies/libspotify/keys/). Just download the key, and save it in the same directory as this readme with the default name (`spotify_appkey.key`), and you're good to go.

## Usage

`python srsly.py -c 35`

Substitute `35` (Sirius XMU) for the channel of your choice, or just run `python srsly.py` to run on the default (35, Sirius XMU).
