import requests


def get(ATURL):
    req = requests.get(ATURL)
    status = req.status_code
    answer =req.json()
    print(status)
    return answer

def cleandata(JSON_response):
    for data in JSON_response['records']:
        i = data['id']
        m = data['fields']['Методы']
        n = data['fields']['Имя']
        ph = data['fields']['Фотография']
        for pp in ph:
            p = pp['url']
        yield {'name':n, 'photo':p, 'method':m, 'recid':i}