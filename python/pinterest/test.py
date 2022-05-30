# # from crypt import methods
# from lib2to3.pgen2 import driver
# import pickle
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# import requests
# import os
# import json

# from flask import Flask, request
# from flask_cors import CORS, cross_origin

# # import uni

# app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

# @app.route('/')
# @cross_origin()
# def entry_point():
#     return "Working ;)"

# @app.route( '/king', methods=["POST"] )
# @cross_origin()
# def fun():
#      is_exist = os.path.exists("cookies.pkl")
#      if not(is_exist):
#         #  uni.login()
     
#              loginbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='RCK Hsu USg adn CCY gn8 L4E kVc iyn oRi lnZ wsz YbY']"))).click()
#              username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='email']")))
#              password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='password']")))
#              username.clear()
#              username.send_keys("amielemeow@gmail.com")
#              password.clear()
#              password.send_keys("Pinklips786")
#     #target the login button and click it
#              button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
#              time.sleep(2)

#              cookies = driver.get_cookies()
#              pickle.dump(cookies,open("cookies.pkl","wb"))

#              time.sleep(2)
#              print("Login")

    

#      def zechking():

#       record = json.loads(request.data)
     
#       if( (not "maal" in record) ):
#         return "Missing Maal <==~"
#       elif (  len(record["maal"]) == 0 ):
#         return "Missing Maal <==~"
#       print(record["maal"])
#       record = record["maal"]
#       url=record
#       site = requests.get(url)
#       mainur=site.url
#       durl = mainur.split("/")[4]

#       print(durl)
#       chrome_options = webdriver.ChromeOptions()
#       chrome_options.add_argument("--headless")
#       chrome_options.add_argument("--disable-dev-shm-usage")
#       chrome_options.add_argument("--no-sandbox")
#       chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#       # driver = webdriver.Chrome('./chromedriver.exe')
#       driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
#       # driver.get(record)
#       driver.get("https://www.pinterest.com")

    
#       cookies = pickle.load(open("cookies.pkl","rb"))
    
#       for c in cookies:
#         c['domain'] = ".pinterest.com"
#         driver.add_cookie(c)

#       time.sleep(2)
#       #  record = '836402962052988516' 
#       url = "https://www.pinterest.com/pin/"+durl
 
#       driver.get(url)

#       v="/html/body/script"
#       inputs = driver.find_element_by_xpath("//script[@type='application/json']")
  

#       stud_obj = json.loads(inputs.get_attribute('innerHTML'))   
   
#       downloadurl=stud_obj["props"]["initialReduxState"]["pins"][durl]["videos"]["video_list"]["V_720P"]["url"]
#       driver.close()
#       return {"video_url":downloadurl}
  
   
#      res=zechking()
#      print(res)
#      return {"download_url" : res}


   
# # print("Finished!")
# if __name__ == "__main__":
#     app.run(debug=True)


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
def fun():
  

    

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
      urlo=record
      # urlo='https://pin.it/4aGyOxz'
      url=urlo
      site = requests.get(url)
      mainur=site.url
      durl = mainur.split("/")[4]


      print(url)
      site = requests.get("https://www.pinterest.com/pin/"+durl)
      mainur=site.url
      print(mainur)
      r=requests.get(mainur)
      soup=BeautifulSoup(r.content,'html.parser')
      script=soup.find('script',{"id":"__PWS_DATA__"}).text

      data=json.loads(script)
# print(script)
      downloadurl=data["props"]["initialReduxState"]["pins"][durl]["videos"]["video_list"]["V_720P"]["url"]
# url=data['video_url']
      # time.sleep(15)
      print(downloadurl)
      

      return {"video_url":downloadurl}


     res=zechking()
     print(res)
     return {"download_url" : res}


   
# print("Finished!")
if __name__ == "__main__":
    app.run(debug=True)


