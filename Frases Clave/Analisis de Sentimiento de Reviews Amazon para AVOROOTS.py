# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:28:32 2022

@author: Ivan Tonatiuh
"""

import pandas as pd
df = pd.read_csv('reviews.csv')
df.head()

#%% quitar texto de estrellas
aux_list=[]
for m in df["stars"]:
    m=float(m.replace(" de 5 estrellas",""))
    
    aux_list.append(m)
    
df["rating"]=aux_list
    
    
#%%

#importamos más librerias

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
#%matplotlib inline

color = sns.color_palette()
py.init_notebook_mode(connected=True)

#Calificaciones de los productos
fig = px.histogram(df, x = "rating")
fig.update_layout(title_text = "Calificación del Producto")
fig.show()    



#%%

df=df.dropna()

import nltk
from nltk.corpus import stopwords
import wordcloud
from wordcloud import WordCloud, STOPWORDS

#nltk.download('stopwords')

#Creamos la lista de palabras

stopwords = set(stopwords.words('spanish'))
stopwords.update(["br", "href"])
#%%
text = " ".join(review for review in df.comment)
wordcloud = WordCloud(stopwords=stopwords).generate(text)

plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()



#%%


#asignamos reseñas con score > 3 como sentimiento positivo
#Score < 3 serán sentimientos negativos
#eliminamos los con score = 3

df = df[df['rating']!=3]
df['sentiment'] = df['rating'].apply(lambda rating: +1 if rating > 3 else -1)




#%%


# partimos el df en positivo y negativo
positive = df[df['sentiment'] == 1]
negative = df[df['sentiment'] == -1]


#%%

pos = " ".join(review for review in positive.comment)
wordcloud2 = WordCloud(stopwords=stopwords).generate(pos)
plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis("off")
plt.show()

#%%

neg = " ".join(str(review) for review in negative.comment)
wordcloud3 = WordCloud(stopwords=stopwords).generate(neg)

plt.imshow(wordcloud3, interpolation='bilinear')
plt.axis("off")
#plt.savefig('wordcloud33.png')
plt.show()

#%%

df['sentimentt'] = df['sentiment'].replace({-1 : 'negative'})
df['sentimentt'] = df['sentimentt'].replace({1 : 'positive'})
fig = px.histogram(df, x="sentimentt")
fig.update_traces(marker_color="indianred",marker_line_color='rgb(8,48,107)',
marker_line_width=1.5)
fig.update_layout(title_text='Product Sentiment')
fig.show()
#%%
def remove_punctuation(text):
    final = "".join(u for u in text if u not in ("?", ".", ";", ":", "!",'"'))
    return final

df['Text'] = df["comment"].apply(remove_punctuation)

#%%

dfNew = df[['comment','sentiment']]
dfNew.head()


#%%

# random split train and test data
import numpy as np
index = df.index
df['random_number'] = np.random.randn(len(index))
train = df[df['random_number'] <= 0.8]
test = df[df['random_number'] > 0.8]

#%%

# count vectorizer:
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
train_matrix = vectorizer.fit_transform(train['comment'])
test_matrix = vectorizer.transform(test['comment'])



#%%# Logistic Regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()


#%%



X_train = train_matrix
X_test = test_matrix
y_train = train['sentiment']
y_test = test['sentiment']

#%%


lr.fit(X_train,y_train)

#%%


predictions = lr.predict(X_test)

#%%


# find accuracy, precision, recall:
from sklearn.metrics import confusion_matrix,classification_report
new = np.asarray(y_test)
confusion_matrix(predictions,y_test)

#%%

print(classification_report(predictions, y_test))
