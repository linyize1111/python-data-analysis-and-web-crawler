my_headers = [
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
'Opera/9.25 (Windows NT 5.1; U; en)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

proxy_list = [
'183.95.80.102:8080',
'123.160.31.71:8080',
'115.231.128.79:8080',
'166.111.77.32:80',
'43.240.138.31:8080',
'218.201.98.196:3128',
'113.195. 225.9 9 : 9999',
'182.34.22.109: 9999',
'18 3.166.97.105 : 9999',
'183 .166.20.162: 9999',
'14.20.235.99: 808'
]



import random
import urllib.request as req
import time
import json
t = 0.1

url="https://medium.com/_/graphql"


proxy = random.choice(proxy_list)
header = random.choice(my_headers)

urlhandle = req.ProxyHandler({'http': proxy})
opener = req.build_opener(urlhandle)
req.install_opener(opener)
request=req.Request(url,headers={
    'User-Agent':header,
    'content-type':"application/json"
    })
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
    

data=json.loads(data)

posts=data["{data: {,…}}"]["data: {,…}"]["extendedFeedItems"]
for key in posts:
    time.sleep(t)
    post=posts[key]["post"]
    print(post["title"])
    