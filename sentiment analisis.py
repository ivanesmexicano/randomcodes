# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:12:49 2022

@author: Ivan Tonatiuh
"""

pip install sentiment-analysis-spanish
pip install keras tensorflow


#%%

from sentiment_analysis_spanish import sentiment_analysis

#%%

sentiment = sentiment_analysis.SentimentAnalysisSpanish()

print(sentiment.sentiment("detesto la porqueria maldita de la tombola"))





#%%


#sentiment = sentiment_analysis.SentimentAnalysisSpanish()
print(sentiment.sentiment("bien esto que me estás diciendo"))
