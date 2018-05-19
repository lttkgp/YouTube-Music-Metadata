from bs4 import BeautifulSoup
import requests

from addons.spotify import search_sp
from addons.musixmatch import search_mm

REQUESTS_SESSION = requests.Session()

def youtube_attached_metadata(song_link):
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
    yt_data = youtube_attached_metadata(song_link)
    sp_data = search_sp(yt_data['song'] + " - " + yt_data['album'])
    mm_data = search_mm(yt_data['song'] + " - " + yt_data['album'])
    return [yt_data, sp_data, mm_data]

if __name__ == "__main__":
    song_link = "https://www.youtube.com/watch?v=zwHF2y2ceSc&feature=share"
    get_metadata(song_link)
