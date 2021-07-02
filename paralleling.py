from tqdm.auto import tqdm
from multiprocessing.pool import ThreadPool



def composeInParallel(array, keys_function, values_function, description, threads=8):
	
	result_pairs = []
	
	for pair in tqdm(
		ThreadPool(threads).imap_unordered(
			lambda e: (keys_function(e), values_function(e)),
			array
		),
		desc=description,
		total = len(array)
	):
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
		total = len(array)
	):
		result_pairs.append(pair)

	return dict(result_pairs)