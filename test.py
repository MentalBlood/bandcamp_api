import main as api
import json



artists = [
	'hiemal',
	'archean nights',
	'winterblood',
	'death on cassete',
	'akhlys',
	'frontierer'
]

result = api.compose(artists, api.getArtistTrueName, api.getAlbums, 'Geting artists albums')

with open('output.json', 'w', encoding='utf8') as f:
	json.dump(result, f, indent=4)