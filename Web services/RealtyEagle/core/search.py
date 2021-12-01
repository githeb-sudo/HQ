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



"""
Variables: proposed_price(), apport_complementaire
Input: duree_2possession
From databases: id, price, surface, prix_2ref_moyen_m2,val_loc_indicative_m2, url2post,estate_postalcode

other existing information 
        # estate_type
        # distribution_type: 1 location, 2 vente
        # photos_nb
        # floor_nb
        # nb_rooms
        # nb_bedrooms

Might be useful if found: 
        # historique/ the amount deemed necessary for repairs
        # Economy/ Market outlook on real estate
        # Future estimations of demographics, Government Policies

"""


duree_pret_en_Mois=180
interets=1.03
interets_mensuel=interets/1200
assurance_Pret=0.273
caution_PPD,levee_PPD=2500,2500
penalités_RA=0.03

annuite=interets_mensuel/(1-(1+interets_mensuel)**(-duree_pret_en_Mois))


frais_dagence=10000
pourcentage_commission=0.0799
charge=75
taux_fonciere=33.3

taux_occupation=0.8

class Bien():
    def __init__(self,apport_complementaire,price,surface,estate_postalcode,url2post,prix_2ref_moyen_m2,val_loc_indicative_m2):

        self.price=price
        self.surface=surface
        self.estate_postalcode=estate_postalcode
        self.url2post=url2post

        self.apport_complementaire=apport_complementaire

        self.prix_2ref_moyen_m2=int(prix_2ref_moyen_m2)
        self.val_loc_indicative_m2=val_loc_indicative_m2

    market_value=lambda self:self.prix_2ref_moyen_m2*self.surface 
    worth_it=lambda self:True                            # when acquiring more accurate gov data self.market_value()>0.9*self.price 

    proposed_price=lambda self:  self.price*0.9          # when acquiring more accurate gov data self.market_value()*0.9

    get_apport_aubanque=lambda self:0.2*self.proposed_price()+self.apport_complementaire
    #+pourcentage_commission*(self.proposed_price()-frais_dagence)

    get_emprunte=lambda self:self.proposed_price()-self.get_apport_aubanque()
    get_price_per_m2=lambda self:self.price/self.surface
    get_prix_propose_par_m2=lambda self:self.proposed_price()/self.surface
    get_mensualites_pret=lambda self:self.get_emprunte()*annuite
    get_mensualites_assu=lambda self:self.get_emprunte()*assurance_Pret/1200

    get_loyer_bas=lambda self:self.surface*self.val_loc_indicative_m2+0.6*charge
    get_loyer_haut=lambda self:self.get_loyer_bas()+0.4*charge+taux_fonciere

    
    
    def residuel(self,duree_2possession):
        return self.residuel(duree_2possession-1)*(interets_mensuel+1)-annuite*self.get_emprunte() if duree_2possession>=1 else self.get_emprunte()

    get_capital_rembourse=lambda self,duree_2possession:self.get_emprunte()-self.residuel(duree_2possession)

    get_plus_value=lambda self:0.2*self.proposed_price()
    """
    Assiette pour l'impôt sur le revenu 0% pour une detention de moins de 6 ans, 
                                        6% pour une detention de la 6e à la 21e année,(pour chaque annee apres la 6e)   
                                        4% pour la 22e année
                                        Exonération au delà de la 22e année

    """
    abattement=lambda self,detention_enannee: self.get_plus_value()*np.where(detention_enannee<6,0,np.where(detention_enannee<=21,6,4))*(detention_enannee-6+1)/100     
    get_impots_plus_value=lambda self,duree_2possession:( self.get_plus_value()-self.abattement(np.floor(duree_2possession/12)))*19/100 if duree_2possession<264 else 0 # Exonération au delà de la 22e année de detention

    get_frais_notaire=lambda self:(self.proposed_price()-frais_dagence)*pourcentage_commission # l'historique est indisponible pour le moment pour un np.where(historique=="Ancien",0.0799,0.02)
   
   
    get_revenu_aumois_i=lambda self,duree_2possession:taux_occupation*duree_2possession*self.get_loyer_bas()+(2-penalités_RA)*(self.get_emprunte()-self.residuel(duree_2possession))+self.get_plus_value()-self.get_impots_plus_value(duree_2possession)+duree_2possession*(self.get_mensualites_pret()-taux_fonciere-charge)-self.get_mensualites_assu()-self.get_frais_notaire()-frais_dagence-levee_PPD*2

    get_=lambda self,duree_2possession: self.get_emprunte()-self.residuel(duree_2possession)+self.get_plus_value()-self.get_impots_plus_value(duree_2possession)-(self.residuel(duree_2possession)-self.get_emprunte()-self.get_mensualites_pret()*duree_2possession)-self.get_mensualites_assu()-self.get_frais_notaire()-frais_dagence-penalités_RA*(self.get_emprunte()-self.residuel(duree_2possession))-levee_PPD*2-taux_fonciere*duree_2possession-charge*duree_2possession


    get_revenu_max_aumois_i=lambda self,duree_2possession:taux_occupation*duree_2possession*self.get_loyer_haut()+(2-penalités_RA)*(self.get_emprunte()-self.residuel(duree_2possession))+self.get_plus_value()-self.get_impots_plus_value(duree_2possession)+duree_2possession*(self.get_mensualites_pret()-taux_fonciere-charge)-self.get_mensualites_assu()-self.get_frais_notaire()-frais_dagence-levee_PPD*2





#----------------------------------------------------------------------------------------------------------------------
scrapped_data='scrapped_data.csv'
data=pd.read_csv("C:/Apache24/htdocs/RealtyEagle/dataset/"+scrapped_data)
#data=pd.read_csv("/content/"+scrapped_data)
data.columns


# id_solo photos_nb floor_nb estate_postalcode url2post

parameter_s_keys=["distribution_type","region","estate_type","nb_rooms","nb_bedrooms","space","price","duree_2possession"]
parser = argparse.ArgumentParser()

for i in range(len(parameter_s_keys)):
    parser.add_argument('-'+parameter_s_keys[i])
namespace = parser.parse_args()
parameters=namespace.__dict__
locals().update(parameters)

duree_2possession=int(duree_2possession)

#parameters.pop('x',"") x notrequired
#check_all(parameters)

scrapped_parameters=parameters
scrapped_parameters.pop("duree_2possession")

operation=dict(zip(parameter_s_keys, [" == "," in "," in "," in "," == "," >= "," >= "," == "]))


query='region>0'+" ".join(" and "+key+" "+operation[key]+" "+str(value) for key,value in scrapped_parameters.items() if (value!='' and value!='[]' and value!=None))



#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    print(data.query(query))
######print((data.query(query)).to_string())
#-----------------------------------------------------------
filtred=data.query(query)

prix_moyen_2vente_m2='dvf-communes-2019.csv'
data_ref=pd.read_csv("C:/Apache24/htdocs/RealtyEagle/dataset/"+prix_moyen_2vente_m2)

lines=data_ref['ID;INSEE_COM;INSEE_DEP;INSEE_REG;CODE_EPCI;NOM_COM_M;POPULATION;Nb_Ventes;PrixMoyen_M2']

info={}
for i in lines:
  prix=i[i.rfind(";")+1:]
  info[i[18:23]]=int(prix) if (prix!='NA') else 0


filtred['prix_2ref_moyen_m2']=[info.get(str(i),0) for i in filtred['estate_postalcode']]




"""
Bien inputs: 
        proposed_price,apport_complementaire,price,surface,estate_postalcode,url2post,prix_2ref_moyen_m2,val_loc_indicative_m2

UI exec passed parameters: 
        distribution_type,region,estate_type,nb_rooms,nb_bedrooms,space,price,duree_2possession

dataframe columns:(scrapped_data.csv + dvf-communes-2019) filtred.iterrows()
        still exist:
        ####################################price                                                             
        estate_type                                                           
        distribution_type                                                    
        ####################################space                                                                 
        id_solo                                                        
        photos_nb                                                            
        floor_nb                                                              
        nb_rooms                                                              
        nb_bedrooms                                                           
        estate_postalcode                                                 
        ####################################url2post              
        region                                                                
        ####################################prix_2ref_moyen_m2
"""
def final():
  for i in filtred.iterrows():
      yield (Bien(40000 ,i[1][0],i[1][3],i[1][9],i[1][10],i[1][12],22)).get_revenu_aumois_i(duree_2possession),(Bien(40000 ,i[1][0],i[1][3],i[1][9],i[1][10],i[1][12],22)).get_revenu_max_aumois_i(duree_2possession), (Bien(40000 ,i[1][0],i[1][3],i[1][9],i[1][10],i[1][12],22)).worth_it()

filtred['gain']=[i[0] for i in final()]
filtred['gain_max']=[i[1] for i in final()]
filtred['worthit']=[i[2] for i in final()]


filtred=filtred.query('gain>0') # filtred.query('worthit==True')

print((filtred).to_string())





