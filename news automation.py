# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 08:27:53 2022

@author: Ivan Tonatiuh
"""

import requests
from sys import argv

API_KEY = '111759e93c324c78b8a2fe5a33eed03b'

URL = ('https://newsapi.org/v2/top-headlines?')


def get_artciles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_artciles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "mx",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []
        
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')

def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "es",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=query_parameters)

    sources = response.json()['sources']

    for source in sources:
        print(source['name'])
        print(source['url'])


if __name__ == "__main__":
# =============================================================================
# =============================================================================
#     print(f"Getting news for {argv[0]}...\n")
#     get_artciles_by_category(argv[1])
#     print(f"Successfully retrieved top {argv[0]} headlines")
# =============================================================================
# =============================================================================
    get_artciles_by_query(argv[1])
    # print_sources_by_category("technology")