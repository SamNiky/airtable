from API_airtable import get, cleandata
from SQL_model import updateclear, addclear, addraw, searchclear, removeclear
from settings import ATURL, session
from datetime import datetime


response = get(ATURL)
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
addraw(response)

generator = cleandata(response)
for data in generator:
    if searchclear(data['recid']) is not None:
        updateclear(data['name'], data['photo'], data['method'], data['recid'], date)
        print('Update '+data['recid'])
    else:
        addclear(data['name'], data['photo'], data['method'], data['recid'], date)
        print('Add '+data['recid'])
removeclear(date)
print(date)