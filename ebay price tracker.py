# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 13:08:57 2022

@author: Ivan Tonatiuh
"""


from bs4 import BeautifulSoup
import requests 
import numpy as np
import csv
from datetime import datetime
import unicodedata

LINK = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=telescope&_sacat=0"


def get_prices_by_link(link):
    # get source
    r = requests.get(link)
    # parse source
    page_parse = BeautifulSoup(r.text, 'html.parser')
    # find all list items from search results
    search_results = page_parse.find("ul",{"class":"srp-results"}).find_all("li",{"class":"s-item"})

    item_prices = []

    for result in search_results:
        price_as_text = result.find("span",{"class":"s-item__price"}).text
        print(price_as_text)
        if "a" in price_as_text:
            continue
        if "XN $" in price_as_text:
            price_as_text= price_as_text.replace("MXN $","")
            
            print(price_as_text)
            print(type(price_as_text))
# =============================================================================
#         if " " in price_as_text:
#             price_as_text= price_as_text.replace(" ","")
# =============================================================================
        price_as_text = unicodedata.normalize("NFKD",price_as_text)       
       
#LA LINEA 43 es la clave para convertir todo el texto a unicode normal y poderlo estripear.
        price_as_text=price_as_text.strip()
        print("after strip")
        print(price_as_text)


# =============================================================================
# 
#         try:
#             price = float(price_as_text[1:].replace(",",""))
#             #Do something
#             pass
#         except Exception as e:
#             print("No se pudo")
#             continue
# =============================================================================
            

        price = float(price_as_text[:].replace(" ",""))
        item_prices.append(price)
        print(price)
    return item_prices

def remove_outliers(prices, m=2):
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def get_average(prices):
    return np.mean(prices)

def save_to_file(prices):
    fields=[datetime.today().strftime("%B-%D-%Y"),np.around(get_average(prices),2)]
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

if __name__ == "__main__":
    prices = get_prices_by_link(LINK)
    prices_without_outliers = remove_outliers(prices)
    print(get_average(prices_without_outliers))
    save_to_file(prices)