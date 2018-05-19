import pytest

from youtube_music_metadata.core import get_youtube_metadata

def test_fetch_youtube_metadata():
    yt_data = get_youtube_metadata("https://www.youtube.com/watch?v=zwHF2y2ceSc&feature=share")
    assert yt_data['song'] == 'Zionsville'
    assert yt_data['artist'] == 'Khruangbin'
    assert yt_data['album'] == 'The Universe Smiles Upon You'
