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
            if org['name'] == 'DevNet Sandbox':
               orgID = org['id']
except Exception as ex:
    print(ex)

endpoint2 = f"/organizations/{orgID}/networks"

try:
    response = requests.get(url=f"{base_url}{endpoint2}", headers=headers)
    if response.status_code == 200:
        nets = response.json()
        for net in nets:
            if net['name'] == 'DevNet Sandbox ALWAYS ON':
                netID = net['id']
except Exception as ex2:
    print(ex2)

endpoint3 = f"/networks/{netID}/devices"

local_inventory = []

try:
    response = requests.get(url=f"{base_url}{endpoint3}", headers=headers)
    if response.status_code == 200:
        devices = response.json()
        for device in devices:
                local_inventory.append({
                  'name' : device['name'],
                  'type' : device['model'],
                  'mac_address' : device['mac'],
                  'serial' : device['serial']
                })
except Exception as ex3:
    print(ex3)

for local_device in local_inventory:
     print(json.dumps(local_device))
