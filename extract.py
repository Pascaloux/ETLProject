# Import des librairies
import pandas as pd
import bs4
import requests
from urllib import request


def extract_date_valeurs_foncieres():
    
    print("Extraction de la date de mise à jour des valeurs foncières")
    
    # Webscrapping pour récupérer la date de mise à jour des données sur les valeurs foncières
    url = "https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/"
    html_data = request.urlopen(url).read()
    soup = bs4.BeautifulSoup(html_data, "lxml")
    row  = soup.find_all('div',{'class' : 'fr-text--sm fr-mb-0 text-grey-380'})[0]
    date = ' '.join(row.getText().strip().split()[4:7])
    return date


def extract_valeurs_foncieres():
    
    print("Extraction des valeurs foncières")
    
    # Lien des valeurs foncières en 2021
    url = 'https://www.data.gouv.fr/fr/datasets/r/817204ac-2202-4b4a-98e7-4184d154d98c'

    # Enregistrement des données dans un dataframe avec le bon format date
    df = pd.read_csv(url, delimiter='|', parse_dates=['Date mutation'], dayfirst=True)

    return df


def extract_capitaux():

    print("Extraction du classement des plus grosses banques")

    url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
    html_data = request.urlopen(url).read()
    soup = bs4.BeautifulSoup(html_data, "lxml")
    Noms=[]
    Capitalisation = []
    for row in soup.find_all('tbody')[3].find_all('tr')[1:]:
        Noms.append(row.find_all('td')[1].getText().rstrip('\n')) 
        Capitalisation.append(row.find_all('td')[2].getText().rstrip('\n'))
    data = pd.DataFrame({"Name" : Noms, "Market Cap (US$ Billion)" : Capitalisation})
    data["Market Cap (US$ Billion)"]= data["Market Cap (US$ Billion)"].str.replace(r"\[.*\]","")
    return data


def extract_taux():

    print("Extraction des taux de change")

    url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=q2RtvboFr7QloNcorghYyDhcMgKl5YKc"
    req = requests.get(url)
    contenu_json = req.json()
    df = pd.DataFrame(contenu_json)
    return df








