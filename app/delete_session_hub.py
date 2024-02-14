import json
import requests

# curl -X "DELETE" http://<your grid IP>:4444/session/<sessionId>

URL_BASE = 'http://hub-animes-to-watch:4444'

r = requests.get(f'{URL_BASE}/status')
data = json.loads(r.text)
for node in data['value']['nodes']:
    for slot in node['slots']:
        if slot['session']:
            id = slot['session']['sessionId']
            r = requests.delete(f"{URL_BASE}/session/{id}")
            print(r)
            print(r.text)

