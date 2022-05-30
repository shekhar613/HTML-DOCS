# from crypt import methods
from lib2to3.pgen2 import driver
import pickle
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import json

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
def fun():
     is_exist = os.path.exists("cookies.pkl")
     if not(is_exist):
        #  uni.login()
     
             username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
             password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    #enter username and password
             username.clear()
             username.send_keys("amielemeow")
             password.clear()
             password.send_keys("Pinklips786")

             #target the login button and click it
             button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
             time.sleep(5)

             cookies = driver.get_cookies()
             pickle.dump(cookies,open("cookies.pkl","wb"))
    
             time.sleep(10)
             print("Login")


    

     def zechking():

      record = json.loads(request.data)
      if( (not "maal" in record) ):
        return "Missing Maal <==~"
      elif (  len(record["maal"]) == 0 ):
        return "Missing Maal <==~"
      print(record["maal"])
      record = record["maal"]
      
      # xpath='/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/video/source'
      # ypath='/html/body/div[1]/section/div[1]/div/div[5]/section/div/div[1]/div/div/video/source'
      # if durl=="highlights":xpath
      # elif durl!="highlights":ypath
      # chrome_options = webdriver.ChromeOptions()
      # chrome_options.add_argument("--headless")
      # chrome_options.add_argument("--disable-dev-shm-usage")
      # chrome_options.add_argument("--no-sandbox")
      # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
      driver = webdriver.Chrome('./chromedriver.exe')
      # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
      # driver.get(record)
      driver.get("https://www.instagram.com")

      time.sleep(2)
      cookies = pickle.load(open("cookies.pkl","rb"))
    
      for c in cookies:
         c['domain'] = ".instagram.com"
         driver.add_cookie(c)

      time.sleep(2)
      driver.get(record)
      # v="/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/video/source"
      # inputs = driver.find_element(by=By.XPATH, value=v)
      time.sleep(5)
      button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()
      img=driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/img")
      imgurl=img.get_attribute('src')
      inputs = driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/video/source")
      
      url=inputs.get_attribute('src')
      # inputs = driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/video/source")
      # inputs=driver.find_element_by_class_name("y-yJ5  OFkrO")
      # inputs= WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "video[class='y-yJ5  OFkrO ']")))
      print(inputs)                          
      
      
      # stud_obj = json.loads(url)   
      print(url)
      print(imgurl)
      # links = stud_obj["items"][0]["video_versions"][0]["url"]
      # links2 = stud_obj["items"][0]["image_versions2"]["candidates"][0]["url"]
      # links3 = stud_obj["items"][0]["user"]["full_name"]
  
      # print(links)
      # print(links2)
      return url,imgurl


     res=zechking()
     print(res)
     return {"download_url" : res}


   
# print("Finished!")
if __name__ == "__main__":
    app.run(debug=True)

