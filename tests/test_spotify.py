import os
from os.path import abspath, dirname, join
from dotenv import load_dotenv
import pytest

DOTENV_PATH = join(dirname(dirname(abspath(__file__))), '.env')
load_dotenv(DOTENV_PATH)

from youtube_music_metadata.addons.spotify import search_sp

def test_fetch_spotify_metadata():
    sp_data = search_sp("Khruangbin - Zionsville")
    assert sp_data['tracks']['total'] == 2
