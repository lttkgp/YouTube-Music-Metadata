import os
from os.path import abspath, dirname, join
from dotenv import load_dotenv
import pytest

DOTENV_PATH = join(dirname(dirname(abspath(__file__))), '.env')
load_dotenv(DOTENV_PATH)

from youtube_music_metadata.addons.musixmatch import search_mm

def test_fetch_spotify_metadata():
    sp_data = search_mm("Seoul - Stay with us")
    assert sp_data['message']['header']['available'] == 10
