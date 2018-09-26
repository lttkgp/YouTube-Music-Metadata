from __future__ import print_function, absolute_import
from bs4 import BeautifulSoup
import requests
from youtube_title_parse import get_artist_title
import argparse

try:
    from youtube_music_metadata.addons.spotify import search_sp
    from youtube_music_metadata.addons.musixmatch import search_mm
except ModuleNotFoundError:
    from addons.spotify import search_sp
    from addons.musixmatch import search_mm

REQUESTS_SESSION = requests.Session()

def get_youtube_metadata(song_link):
    yt_data = {}
    yt_page = REQUESTS_SESSION.get(song_link).text
    soup = BeautifulSoup(yt_page, 'html.parser')
    yt_title = soup.find('meta', {'property': 'og:title'}).get('content').strip()
    yt_data['title'] = yt_title
    yt_metadata = soup.find('div', id='watch-description-extras').find(
        'ul', {'class': 'watch-extras-section'}).find_all('li', {'class': 'watch-meta-item'})
    for metadata in yt_metadata:
        if metadata.find('h4', {'class': 'title'}).get_text().strip() == 'Song':
            song_name = metadata.find('ul', {'class': 'content'}).get_text().strip()
            yt_data['song'] = song_name
        elif metadata.find('h4', {'class': 'title'}).get_text().strip() == 'Artist':
            artist_name = metadata.find('ul', {'class': 'content'}).get_text().strip()
            yt_data['artist'] = artist_name
        elif metadata.find('h4', {'class': 'title'}).get_text().strip() == 'Album':
            album_name = metadata.find('ul', {'class': 'content'}).get_text().strip()
            yt_data['album'] = album_name
    return yt_data

def get_metadata(song_link, spotify=False, musixmatch=False):
    metadata = {}
    if 'youtube.com' not in song_link and 'youtu.be' not in song_link:
        metadata['youtube'] = {}
        metadata['spotify'] = {}
        metadata['musixmatch'] = {}
        return metadata
    yt_data = get_youtube_metadata(song_link)
    clean_title = get_artist_title(yt_data['title'])
    metadata['youtube'] = yt_data
    if 'artist' not in yt_data:
        if spotify == True:
            sp_data = search_sp(clean_title)
            metadata['spotify'] = sp_data
        if musixmatch == True:
            mm_data = search_mm(clean_title)
            metadata['musixmatch'] = mm_data
    elif 'artist' in yt_data and 'song' not in yt_data:
        if spotify == True:
            sp_data = search_sp(yt_data['artist'] + " " + clean_title)
            metadata['spotify'] = sp_data
        if musixmatch == True:
            mm_data = search_mm(yt_data['artist'] + " " + clean_title)
            metadata['musixmatch'] = mm_data
    else:
        if spotify == True:
            sp_data = search_sp(yt_data['song'] + " - " + yt_data['artist'])
            metadata['spotify'] = sp_data
        if musixmatch == True:
            mm_data = search_mm(yt_data['song'] + " - " + yt_data['artist'])
            metadata['musixmatch'] = mm_data
    return metadata

def main():
    argparser = argparse.ArgumentParser(
        description='youtube_music_metadata', formatter_class=argparse.RawTextHelpFormatter)
    argparser.add_argument(
        "youtube_link", type=str, help='required youtube video link')
    args = argparser.parse_args()
    song_link = args.youtube_link
    metadata = get_metadata(song_link, spotify=True, musixmatch=True)
    print(metadata)

if __name__ == "__main__":
    main()
