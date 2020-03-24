import requests
import bs4

print("IMAGE CRAWLER by ishandeveloper\n\n")
url = str(input("Enter or Paste the URL: "))
url.strip()

try:
    print("Connecting To The Host .... " + url)
    opener=urllib.request.build_opener()
    opener.add_headers=[{'User-Agent' : 'Mozilla'}]
    urllib.request.install_opener(opener)
    
    raw=requests.get(url).text
    soup=bs4.BeautifulSoup(raw,'html.parser')

    imgs=soup.find_all('img')

    imglinks=[]

    

except: