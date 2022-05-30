from lib2to3.pgen2 import driver
import pickle
import time
from bs4 import BeautifulSoup
import requests
import json
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait

import os


from flask import Flask, request
from flask_cors import CORS, cross_origin

# import uni

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def entry_point():
    return "Working ;)"

@app.route( '/king', methods=["POST"] )
@cross_origin()


    

def zechking():

      record = json.loads(request.data)
      if( (not "maal" in record) ):
        return "Missing Maal <==~"
      elif (  len(record["maal"]) == 0 ):
        return "Missing Maal <==~"
      print(record["maal"])
      record = record["maal"]
     
      # chrome_options = webdriver.ChromeOptions()
      # chrome_options.add_argument("--headless")
      # chrome_options.add_argument("--disable-dev-shm-usage")
      # chrome_options.add_argument("--no-sandbox")
      # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
      # # driver = webdriver.Chrome('./chromedriver.exe')
      # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
      # driver.get(record)
      # driver.get("https://www.instagram.com")

    
      # r=driver.get(record)
      # v="/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/video/source"
      # inputs = driver.find_element(by=By.XPATH, value=v)
      # time.sleep(5)
      # soup=BeautifulSoup(r.content,'html.parser')
      url=record
      print(url)
      site = requests.get(url)
      mainur=site.url
      print(mainur)
      durl = mainur.split("/")[3]
      dur2 = durl.split("=")[1]
      dur3 = dur2.split("&c")[0]
      print(dur3)
      mainurl='https://likee.video/@Akhir./video/'+dur3

      r=requests.get(mainurl)

      soup=BeautifulSoup(r.content,'html.parser')
      script=soup.find_all('script')[4].text.strip()[14:-1]
      
      data=json.loads(script)
      url=data['video_url']
      print(url)
      downloadurl=url.replace('_4','')
      print(downloadurl)

     
      # inputs = driver.find_element_by_xpath("/html/head/script[5]")
      # inputs=driver.find_element_by_class_name("y-yJ5  OFkrO")
      # inputs= WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "video[class='y-yJ5  OFkrO ']")))
      # print(inputs)                          
      # url=inputs.get_attribute('text()')
      # url= json.loads(inputs.get_attribute('innerHTML'))   
      # stud_obj = json.dumps(url)   
      # print(url)
      # links = stud_obj["items"][0]["video_versions"][0]["url"]
      # links2 = stud_obj["items"][0]["image_versions2"]["candidates"][0]["url"]
      # links3 = stud_obj["items"][0]["user"]["full_name"]
  
      # print(links)
      # print(links2)
      return {'download_url':downloadurl}


    #  res=zechking()
    #  print(res)
    #  return {"download_url" : res}


   
# print("Finished!")
if __name__ == "__main__":
    app.run(debug=True)
