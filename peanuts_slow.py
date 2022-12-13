from selenium import webdriver
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import requests
import shutil
import os

today = str(date.today()).split("-")
year = today[0]
month = today[1]
day = today[2]

mesi = {
    "01": "gennaio",
    "02": "febbraio",
    "03": "marzo",
    "04": "aprile",
    "05": "maggio",
    "06": "giugno",
    "07": "luglio",
    "08": "agosto",
    "09": "settembre",
    "10": "ottobre",
    "11": "novembre",
    "12": "dicembre"
}


url_today = "https://www.ilpost.it/"+year+"/"+month+"/"+day+"/"+"peanuts-"+year+"-"+mesi[month]+"-"+day

file_name ="/home/fradepe/Immagini/Peanuts/Peanuts-"+day+"-"+month+"-"+year+".jpg"
short_file_name = "Peanuts-"+day+"-"+month+"-"+year+".jpg"

if short_file_name in os.listdir("/home/fradepe/Immagini/Peanuts/"):

    print("Striscia già salvata")
    quit()

#option = Options()
#option.add_argument("-headless")

#driver = webdriver.Firefox(options=option)
driver = webdriver.Firefox()
driver.get(url_today)

image = driver.find_element(By.CLASS_NAME, 'wp-post-image')

url_img = image.get_attribute('src')

response = requests.get(url_img, stream=True)

with open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

driver.close()
