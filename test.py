import main as api
import json
from tqdm.auto import tqdm
from multiprocessing.pool import ThreadPool



def processInParallel(array, function, description, threads=8):
	for result in tqdm(
		ThreadPool(threads).imap_unordered(
			function,
			array
		),
		desc=description,
		total = len(array) if type(array) == list else None):
		pass


def composeInParallel(array, function, description, threads=8):
	
	result_pairs = []
	
	for pair in tqdm(
		ThreadPool(threads).imap_unordered(
			lambda e: (e, function(e)),
			array
		),
		desc=description,
		total = len(array) if type(array) == list else None):
		result_pairs.append(pair)

	return dict(result_pairs)


def composeSequentially(array, keys_function, values_function, description, threads=8):

	result_pairs = []
	
	for pair in tqdm(
		map(
			lambda e: (keys_function(e), values_function(e)),
			array
		),
		desc=description,
		total = len(array) if type(array) == list else None):
		result_pairs.append(pair)

	return dict(result_pairs)

compose = composeSequentially


artists = [
	'hiemal',
	'archean nights',
	'winterblood',
	'death on cassete',
	'akhlys',
	'frontierer'
]

result = compose(artists, api.getArtistTrueName, api.getAlbums, 'Geting artists albums')

with open('output.json', 'w', encoding='utf8') as f:
	json.dump(result, f, indent=4)

api.finish()