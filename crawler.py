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

    for i in imgs:
        link=i.get('src')
        if ('http://' not in link):
            link=url+link
        imglinks.append(link)

    print('\n\n'+str(len(imglinks))+' Images Found.\n\n')


    if os.path.isdir('images'):
        shutil.rmtree('images')
    os.mkdir('images')
    i=1
    
    for index, img_link in enumerate(imglinks):
        if i<=len(imglinks):
            img_data=requests.get(img_link).content
            with open("images\\"+str(index+1)+".png","wb+") as f:
                f.write(img_data)
                print('Saving images '+str(i)+' of '+str(len(imglinks)), end="\r")
                i+=1
                
        else:
            print('Task Completed')
            f.close()
            break
        
    print('\n\nMade by Ishan Sharma(github.com/ishandeveloper)')

except:
    print("Oops! An unknown error has occurred or maybe you just entered an Invalid URL :D")
    