from getPage import getPageSelenium as getPage, finish
import json



def getArtistUrl(artist_name):

	search_page = getPage(f'https://bandcamp.com/search?q={artist_name}')
	search_results_elements = search_page.select('.searchresult')
	
	albums_elements = [*filter(
		lambda e: json.loads(e['data-search'])['type'] == 'a', 
		search_results_elements
	)]
	if len(albums_elements):
		first_album_url = albums_elements[0].select('.itemurl')[0].text
		first_album_artis_url = first_album_url.strip().split('bandcamp.com')[0] + 'bandcamp.com'
		return first_album_artis_url
	
	artists_elements = [*filter(
		lambda e: json.loads(e['data-search'])['type'] == 'b', 
		search_results_elements
	)]
	if len(artists_elements):
		first_artist_url = artists_elements[0].select('.itemurl')[0].text.strip()
		return first_artist_url

	return None


def _getAlbumTitleFromElement(element):
	title_text = element.select('.title')[0].text
	title_text_first_line = title_text.strip().split('\n')[0]
	return title_text_first_line


def getAlbums(artist_name_or_url):

	artist_url = artist_name_or_url if artist_name_or_url.endswith('bandcamp.com') else getArtistUrl(artist_name_or_url)
	artist_music_page = getPage(f'{artist_url}/music')
	albums_links_elements = artist_music_page.select('.music-grid-item > a')
	
	return {
		_getAlbumTitleFromElement(e): {
			'link': artist_url + e['href']
		} for e in albums_links_elements
	}


def getArtistTrueName(artist_name_or_url):
	artist_url = artist_name_or_url if artist_name_or_url.endswith('bandcamp.com') else getArtistUrl(artist_name_or_url)
	artist_music_page = getPage(f'{artist_url}/music')
	artist_true_name = artist_music_page.select('#band-name-location .title')[0].text.strip()
	return artist_true_name