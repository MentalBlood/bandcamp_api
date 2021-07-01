import requests
from bs4 import BeautifulSoup
import json



def getArtistUrl(artist_name):
	
	search_request = requests.get(f'https://bandcamp.com/search?q={artist_name}')
	search_page = BeautifulSoup(search_request.text, 'html.parser')
	search_results_elements = search_page.select('.searchresult')
	
	artists_elements = [*filter(
		lambda e: json.loads(e['data-search'])['type'] == 'b', 
		search_results_elements
	)]
	first_artist_url = artists_elements[0].select('.itemurl')[0].text
	
	return first_artist_url.strip()


def getAlbums(artist_name_or_url, artist_url=None):

	artist_url = artist_name_or_url if artist_name_or_url.endswith('bandcamp.com') else getArtistUrl(artist_name_or_url)
	artist_request = requests.get(artist_url)
	artist_page = BeautifulSoup(artist_request.text, 'html.parser')
	albums_links_elements = artist_page.select('.music-grid-item > a')
	# print(albums_links_elements)
	
	return {
		e.select('.title')[0]: {
			'link': artist_url + e['href']
		} for e in albums_links_elements
	}



result = getAlbums('hiemal')
print(result)
# print(json.dumps(result, indent=4))