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


# aaa = get(URL_REQ, BASE_ID, TABLE_NAME, API_KEY)
# ccc = cleandata(aaa)
# # print(ccc)
# for x in ccc:
#     if qur(x['i']) is not None:
#         print('true')
#         nam = x['n']
#         print(nam)
#     else:
#         print('false')

# def test(p, n):
#     print(p)
#     print(n)
#
# sp = {'a':fph, 'b':fname}
# sp1 = f"aa = {sp['a']}"
# print(sp1)