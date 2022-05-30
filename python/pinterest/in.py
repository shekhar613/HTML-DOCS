from bs4 import BeautifulSoup
import requests
import json

site = requests.get("https://www.tiktok.com/@le20veineux/video/7101711525739580678")
mainur=site.url
print(mainur)
r=requests.get(mainur)
soup=BeautifulSoup(r.content,'html.parser')
# script=soup.find('script',{"id":"SIGI_STATE"}).text
# script=soup.find('html')
# ss=soup.get_text()
# script=soup.text
print(soup)
# data=json.dumps(script)
# print(data)
# downloadurl=data["items"]["0"]["pins"]["video_versions"]["0"]["url"]
# url=data['video_url']
      # time.sleep(15)
# print(downloadurl)
      

  