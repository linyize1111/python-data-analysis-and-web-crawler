import urllib.request as req
import time
t=1
def getData(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
        })
    with req.urlopen(request,timeout = None) as response:
        data=response.read().decode("utf-8")
    
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    #print(root)
    titles=root.find_all("div",class_="title")
    for title in titles:
        if title.a!=None:
            print(title.a.string)
    nextlink=root.find("a",string="‹ 上頁")
    print(nextlink["href"])
    return nextlink["href"]

purl="https://www.ptt.cc/bbs/movie/index.html"    
n=0;
for i in range(5):
    #time.sleep(t)
    #getData(purl)
    purl="https://www.ptt.cc"+getData(purl)
    print(purl)
    
    