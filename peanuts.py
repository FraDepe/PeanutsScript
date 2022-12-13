import requests
from datetime import date
from requests_html import HTMLSession
import shutil
import os
import sys

home_dir = os.path.expanduser('~')

print("Checking if the peanuts folder exists")

if  "Pictures" in os.listdir(home_dir):
    if  "Peanuts" not in os.listdir(home_dir+"/Pictures"):
        
        boolean = input("Peanuts folder doesn't exist. Would you like to create one? [y/n]")
        if boolean == "y" or boolean == "Y":
            print("Creating Peanuts folder")
            os.makedirs(home_dir+"/Pictures/Peanuts")
        else:
            print("Adapt the script")
            quit()

    peanuts_dir = home_dir+"/Pictures/Peanuts"

elif "Immagini" in os.listdir(home_dir):
    if  "Peanuts" not in os.listdir(home_dir+"/Immagini"):

        boolean = input("Peanuts folder doesn't exist. Would you like to create one? [y/n]")
        if boolean == "y" or boolean == "Y":
            print("Creating Peanuts folder")
            os.makedirs(home_dir+"/Immagini/Peanuts")
        else:
            print("Adapt the script")
            quit()

    peanuts_dir = home_dir+"/Immagini/Peanuts"
else:
    print("Your system language is not supported. Please adapt this program")
    #You should change one case and change Pictures or Immagini with your word

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

print("Today is "+str(date.today()))

url_today = "https://www.ilpost.it/"+year+"/"+month+"/"+day+"/"+"peanuts-"+year+"-"+mesi[month]+"-"+day


# Linux systems

if sys.platform == "linux" or sys.platform == "linux2":
    file_name =peanuts_dir+"/Peanuts-"+day+"-"+month+"-"+year+".jpg"
    short_file_name = "Peanuts-"+day+"-"+month+"-"+year+".jpg"

    print("Visiting "+url_today)

    if short_file_name in os.listdir(peanuts_dir):

        print("Illustration already saved")
        quit()

    session = HTMLSession()

    response = session.get(url_today)

    img_html_element = response.html.find('.wp-post-image')

    url_img = img_html_element[0].attrs['src']

    print("Fetching data from the website ")

    response_src = requests.get(url_img, stream=True)

    print("Getting source from"+url_img)

    with open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response_src.raw, out_file)
    del response_src

    print("Illustration saved")


# Windows systems  DA COMPLETARE

elif sys.platform == "win32":

    file_name ="Peanuts-"+day+"-"+month+"-"+year+".jpg"

    print("Visiting "+url_today)

    if file_name in os.listdir("/home/fradepe/Immagini/Peanuts/"):

        print("Illustration already saved")
        quit()

    session = HTMLSession()

    response = session.get(url_today)

    img_html_element = response.html.find('.wp-post-image')

    url_img = img_html_element[0].attrs['src']

    print("Fetching data from the website ")

    response_src = requests.get(url_img, stream=True)

    print("Getting source from"+url_img)

    with open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response_src.raw, out_file)
    del response_src

    print("Illustration saved")

    #with open("/home/fradepe/Coding/Python/Peanuts/site.html", 'w') as file_html:
    #    file_html.write(response.content.decode())

    # wp-post-image
