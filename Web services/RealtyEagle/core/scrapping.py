import html5lib, lxml, requests , re, cloudscraper, os, csv, time, sys, random
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,sys,shlex,subprocess,argparse,time,pandas
from numpy.random import randint
import numpy as np
from socket import timeout

extacted_data='extacted_data.csv'
header=np.where(os.path.exists(extacted_data),0,1)
with open(extacted_data, 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # Other available data: energy_letter, client_type, client_id, position, media
    #writer.writerow(['list_name','position','price','estate_type','distribution_type','space','id','id_solo','client_id','photos_nb','estate_postalcode','client_postalcode','country','client_type','parent_site','floor_nb','nb_rooms','nb_bedrooms','energy_letter','product_status','media','product_type']) if header else None
    writer.writerow(['price','estate_type','distribution_type','space','id_solo','photos_nb','floor_nb','nb_rooms','nb_bedrooms','estate_postalcode','url2post','region']) if header else None
    hourlylimit_supervisor=0
    for code_region in range(1,23):
        page=0
        time.sleep(10)
        
        annonces=[-1] 
        while(annonces!=[]):

            # to avoid being blocked and having to solve captcha            
            # if (hourlylimit_supervisor>390):
            #   hourlylimit_supervisor=0
            #   sleep(7200)


            # random clicks to avoid a detection of a crawling pattern
            

            random_url = f"https://www.logic-immo.com/vente-immobilier-0,{random.randint(1,23)}_0/options/groupprptypesids={random.randint(1,23)}/page={random.randint(1,23)}"
            requests.get(random_url).text

            # to be gentle with the site and to emulate a human behavior
            time.sleep(15) 

            page+=1
            url = f"https://www.logic-immo.com/vente-immobilier-0,{code_region}_0/options/groupprptypesids=1/page={page}"
            scraper = cloudscraper.create_scraper()
            source= scraper.get(url).text

            soup=bs(source,'lxml')
            annonces=soup.find_all("a", class_="add-to-selection")

            for annonce in annonces:    

                hourlylimit_supervisor+=1

                target_field=str(annonce).split("{")[3]
                target_data=re.findall(r':([0-9]+)', target_field)
                target_data.pop(0)                  #remove position
                target_data.pop()                   #remove media
                if (len(target_data)<9):            # -1 if floor_nb is not defined
                    target_data.insert(6,-1) 
                elif (len(target_data)>9):         
                    target_data.pop()

                target_data+=re.findall(r'.*estate_postalcode.:\'([\d]+)', target_field) # Preserve the estate_postalcode
                
                id=target_field[target_field.find("id")+5:target_field.find("id_")-3]
                url2post="https://www.logic-immo.com/detail-vente-"+id+".htm"
                target_data.append(url2post)
                target_data.append(code_region)
                writer.writerow(target_data)
