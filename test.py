import main as api
import json



artists = [
	'akhlys',
	'frontierer'
]

result = {a: api.getAlbums(a) for a in artists}

with open('output.json', 'w', encoding='utf8') as f:
	json.dump(result, f, indent=4)

api.finish()