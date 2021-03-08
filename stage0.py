import requests
import json
from env import config

meraki_key =  config['MERAKI_KEY']
base_url = 'https://api.meraki.com/api/v0'
endpoint = '/organizations'

headers ={
    'X-Cisco-Meraki-API-Key': meraki_key
}

try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        orgs = response.json()
        for org in orgs:
            print("ID is " + str(org['id']) + ", name is " + str(org['name']))
except Exception as ex:
    print(ex)