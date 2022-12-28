# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:03:53 2022

@author: Ivan Tonatiuh
"""

#JOINING texts from motorpasion

#%%


# import necessary libraries
import pandas as pd
import os
import glob
  
  
# use glob to get all the csv files
# in the folder


path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.xlsx"))


 #%% loop
# loop over the list of csv files
for f in csv_files:
    
    # read the csv file
    df = pd.read_excel(f)
      
    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])
      
    # print the content
    print('Content:')
    display(df)
    print()
    
#%%
datos=pd.read_excel("motorpasion.xlsx")
concentrador=pd.DataFrame(datos["header"])


text = " ".join(map(str,(comment for comment in concentrador.header)))
#%%

import matplotlib.pyplot as plt
from wordcloud import WordCloud

import nltk
from nltk.corpus import stopwords
nltk.corpus.stopwords.words("spanish")
stop_words = set(stopwords.words('spanish'))

from nltk.tokenize import word_tokenize

word_tokens = word_tokenize(text)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]


palabras_sin_sentido={",",":",";","si",".","DE","Que","El","Y","La","asi","PARA","ma","Saludo","saludo","Si","solo","q","Lo"}
stop_words.update(palabras_sin_sentido)


filtered_sentence = []

for w in word_tokens:

    if w not in stop_words:

        filtered_sentence.append(w)

text_cap=' '.join(filtered_sentence)


word_cloud = WordCloud(collocations = False, background_color = 'white', width=800, height=400).generate(text_cap)

#%%
plt.figure(figsize=(20,10))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()

plt.savefig('motorpas.png')
