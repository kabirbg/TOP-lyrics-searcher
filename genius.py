from pygenius import *
from api_key import key
import requests

artist_id = 23796 # twenty one pilots artist id, magic number but shouldn't break

response = requests.get(f"http://api.genius.com/artists/{artist_id}/songs")
json_data = response.json()

