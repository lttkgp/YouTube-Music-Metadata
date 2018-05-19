"""
Musixmatch setup
"""
import os
import requests

REQ_SESSION = requests.Session()
MUSIXMATCH_BASE_URL = "http://api.musixmatch.com/ws/1.1/"
MM_API_KEY = os.environ.get("MUSIXMATCH_API_KEY")
SEARCH_ENDPOINT = "track.search"
SEARCH_PARAMS = {
    "apikey": MM_API_KEY
}

def search_mm(query):
    """
    Method to search for a track using Musixmatch API
    """
    SEARCH_PARAMS['q'] = query
    response = REQ_SESSION.get(MUSIXMATCH_BASE_URL + SEARCH_ENDPOINT, params=SEARCH_PARAMS).json()
    return response
