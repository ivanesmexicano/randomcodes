# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:51:43 2022

@author: Ivan Tonatiuh
"""

#%%
import pandas as pd

pd.read_csv("reviews.csv")
#%%

import pandas as pd
import matplotlib as plt

dataset=pd.read_csv("reviews.csv")

summarised_results = dataset["stars"].value_counts()


plt.bar(summarised_results.keys(), summarised_results.values)
plt.show()


#%%

def visualise_word_map():
    words=" "
    for msg in dataset["comment"]:
        msg = str(msg).lower()
            words = words+msg+" "
        wordcloud = WordCloud(width=3000, height=2500, background_color='white').generate(words)
        fig_size = plt.rcParams["figure.figsize"]
        fig_size[0] = 14
        fig_size[1] = 7
        plt.show(wordcloud)
        plt.axis("off")