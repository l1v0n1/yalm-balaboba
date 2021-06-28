import json
import urllib.request

class generation():
  def gen(text):
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 '
                      '(KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Origin': 'https://yandex.ru',
        'Referer': 'https://yandex.ru/',
    }


    API_URL = 'https://zeapi.yandex.net/lab/api/yalm/text3'
    payload = {"query": text, "intro": 0, "filter": 1}
    params = json.dumps(payload).encode('utf8')
    req = urllib.request.Request(API_URL, data=params, headers=headers)
    response = urllib.request.urlopen(req)
    reqst = json.loads(response.read().decode('utf8'))
    query = reqst['query']
    ans = reqst['text']
    return query + ans

if __name__ == "__main__":
    generate = generation.gen('')