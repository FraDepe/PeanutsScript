try:
    import requests
except ModuleNotFoundError:
    print("module 'requests' is not installed")
    quit()
    
from datetime import date

try:
    from requests_html import HTMLSession
except ModuleNotFoundError:
    print("module 'requests_html' is not installed")
    quit()

import json
import shutil
import os
import sys

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

def main():

    #Getting actual date
    today = str(date.today()).split("-")
    year = today[0]
    month = today[1]
    day = today[2]

    # Getting folder to use to store images
    home_dir = os.path.expanduser('~')

    here = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(here, "peanuts_config.json")

    with open(config_path, 'r+') as config_file:

        if os.stat(config_path).st_size > 1:
            peanuts_folder = json.load(config_file)["path"]
        
        else:
            choose = input("Configuration file with directory to store images is empty.\nDo i save in Pictures folder? [y/n] ")
        
            if choose == "y":
        
                if "Pictures" in os.listdir(home_dir):
                    peanuts_folder = home_dir+"/Pictures/Peanuts"
                    os.makedirs(peanuts_folder)
        
                elif "Immagini" in os.listdir(home_dir):
                    peanuts_folder = home_dir+"/Immagini/Peanuts"
                    os.makedirs(peanuts_folder)
                
                else:
                    print("Pictures or Immagini folder doesn't exist. Create it in home or change this script")
                    #You should change one case and change Pictures or Immagini with your word
                    quit()

            elif choose == "n":
                peanuts_folder = input("Type the absolute path you want to use ")
                os.makedirs(peanuts_folder)
            
            else:
                print("Invalid answer")
                quit()
        
            #Saving path in json config
            json.dump({"path": peanuts_folder}, config_file)

    #Starting scraping
    print("Today is "+str(date.today()))

    url_today = "https://www.ilpost.it/"+year+"/"+month+"/"+day+"/"+"peanuts-"+year+"-"+mesi[month]+"-"+day

    file_name =peanuts_folder+"/Peanuts-"+year+"-"+month+"-"+day+".jpg"
    short_file_name = "Peanuts-"+year+"-"+month+"-"+day+".jpg"

    print("Visiting "+url_today)

    if short_file_name in os.listdir(peanuts_folder):

        print("Illustration already saved")
        quit()

    session = HTMLSession()

    response = session.get(url_today)

    img_html_element = response.html.find('.wp-post-image')

    try:
        url_img = img_html_element[0].attrs['src']
        
        print("Fetching data from the website ")

        response_src = requests.get(url_img, stream=True)

        print("Getting source from "+url_img)

        with open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response_src.raw, out_file)
        del response_src

        print("Illustration saved")

    except:
        print("No illustrations have been uploaded today")




def dated(date):
    date = date.split("/")

    #Getting specific url
    year = date[2]
    month = date[1]
    day = date[0]

    # Getting folder to use to store images
    home_dir = os.path.expanduser('~')

    here = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(here, "peanuts_config.json")

    with open(config_path, 'r+') as config_file:

        if os.stat(config_path).st_size > 1:
            peanuts_folder = json.load(config_file)["path"]
        
        else:
            choose = input("Configuration file with directory to store images is empty.\nDo i save in Pictures folder? [y/n] ")
        
            if choose == "y":
        
                if "Pictures" in os.listdir(home_dir):
                    peanuts_folder = home_dir+"/Pictures/Peanuts"
                    os.makedirs(peanuts_folder)
        
                elif "Immagini" in os.listdir(home_dir):
                    peanuts_folder = home_dir+"/Immagini/Peanuts"
                    os.makedirs(peanuts_folder)
                
                else:
                    print("Pictures or Immagini folder doesn't exist. Create it in home or change this script")
                    #You should change one case and change Pictures or Immagini with your word
                    quit()

            elif choose == "n":
                peanuts_folder = input("Type the absolute path you want to use ")
                os.makedirs(peanuts_folder)
            
            else:
                print("Invalid answer")
                quit()
        
            #Saving path in json config
            json.dump({"path": peanuts_folder}, config_file)

    #Starting scraping

    url_today = "https://www.ilpost.it/"+year+"/"+month+"/"+day+"/"+"peanuts-"+year+"-"+mesi[month]+"-"+day

    file_name =peanuts_folder+"/Peanuts-"+day+"-"+month+"-"+year+".jpg"
    short_file_name = "Peanuts-"+day+"-"+month+"-"+year+".jpg"

    print("Visiting "+url_today)

    if short_file_name in os.listdir(peanuts_folder):

        print("Illustration already saved")
        quit()

    session = HTMLSession()

    response = session.get(url_today)

    img_html_element = response.html.find('.wp-post-image')

    try:
        url_img = img_html_element[0].attrs['src']
        
        print("Fetching data from the website ")

        response_src = requests.get(url_img, stream=True)

        print("Getting source from "+url_img)

        with open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response_src.raw, out_file)
        del response_src

        print("Illustration saved")

    except:
        print("No illustrations have been uploaded during this day")

if len(sys.argv) == 1:
    main()
elif len(sys.argv) == 2:
    dated(sys.argv[1])

