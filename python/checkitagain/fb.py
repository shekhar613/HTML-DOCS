from bs4 import BeautifulSoup
import json
import requests

mainurl='https://www.smule.com/p/362363372_3682892532'

r=requests.get(mainurl)
soup=BeautifulSoup(r.content,'html.parser')
# print(soup)
# script=soup.find_all('script')
# script=soup.find('video',{"class":"vjs-tech"})
print(soup)

# vjs_video_3_html5_api