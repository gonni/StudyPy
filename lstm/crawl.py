import requests as req

url = 'http://search.naver.com/search.naver'
res = req.get(url, params={'query': '윤도리'})

print(res.text)
