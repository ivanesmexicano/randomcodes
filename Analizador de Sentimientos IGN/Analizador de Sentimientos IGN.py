# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:37:08 2022

@author: Ivan Tonatiuh
"""


from sentiment_analysis_spanish import sentiment_analysis

#%%

sentiment = sentiment_analysis.SentimentAnalysisSpanish()
print(sentiment.sentiment("me gusta la tombola es genial"))

#%%

print(sentiment.sentiment("me fascina su risa"))


#%%

import pysentimiento
import matplotlib
