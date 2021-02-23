from airtable import airtable
import json
import requests


API_KEY = 'keyJnqTCPtMLLSWyV'
BASE_ID = 'appgru70CpzqkRsg1'
TABLE_NAME = 'Psychotherapists'
fname = 'Имя'
fph = 'Фотография'
fmethod = 'Методы'

# at = airtable.Airtable(BASE_ID, API_KEY)
# a = at.get(TABLE_NAME, view=1, fields=[fname, fmethod])

# print(a)


at = requests.get(f'https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}?api_key={API_KEY}', )
a = at.status_code
b = at.json()

print(a)
for data in b['records']:
    print(type(data['fields']['Методы']))