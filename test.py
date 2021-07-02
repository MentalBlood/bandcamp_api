import main as api
import json

result = api.getAlbums('death on cassete')
with open('output.json', 'w', encoding='utf8') as f:
	json.dump(result, f, indent=4)

api.finish()