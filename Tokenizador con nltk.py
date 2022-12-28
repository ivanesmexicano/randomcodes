# -*- coding: utf-8 -*-
# coding: latin1

"""
Created on Tue Nov  8 10:47:44 2022

@author: Ivan Tonatiuh
"""

from nltk import tokenize
p = "Buenos días, Dr. Adams. El paciente lo espera en el cuarto 3."

tokenize.sent_tokenize(data)





#%%

import unicodedata
import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
fp = open("test.txt", encoding="utf-8")

data = fp.read()
unicodedata.normalize("NFC",data)
print ('\n-----\n'.join(tokenizer.tokenize(data)))


#%% ESTO NO FUE NECESARIO PERO ES UN TIP por si algun día necesitamos codificar o decodificar
sentence=fp

sentence = sentence.decode('latin-1') 
sentence = unicodedata.normalize('NFKD', sentence) 
spaChar = 'á'.decode('latin-1') 
spaChar = unicodedata.normalize('NFKD', spaChar) 
print (spaChar in sentence)



#%%

import stanza

stanza.download('es')
nlp = stanza.Pipeline(lang='es', processors='tokenize')

t_en=data

doc = nlp(t_en)
lisTa=[]
for sentence in doc.sentences:
    lisTa.append(sentence.text)
    print(sentence.text)