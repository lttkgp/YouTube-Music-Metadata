"""
Spotify setup
"""
import os
import spotipy
import spotipy.util as spotipy_util

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.environ.get("SPOTIFY_REDIRECT_URI")
SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME")
SPOTIFY_TOKEN = spotipy_util.prompt_for_user_token(
    SPOTIFY_USERNAME, 'user-read-email', SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI)
SPOTIFY = spotipy.Spotify(auth=SPOTIFY_TOKEN)

def search_sp(query):
    """
    Method to search for a track using Spotify API
    """
    response = SPOTIFY.search(q=query, type='track')
    return response
