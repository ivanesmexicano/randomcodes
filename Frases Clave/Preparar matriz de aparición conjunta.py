# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:48:37 2022

@author: Ivan Tonatiuh
"""

# Python3 program to Check if given words
# appear together in a list of sentence
#%%
def check(sentence, words):
	res = [all([k in s for k in words]) for s in sentence]
	return [sentence[i] for i in range(0, len(res)) if res[i]]
	


#%% hacer matrix de frases


import numpy as np
import pandas as pd

location="C:/Users/Ivan Tonatiuh/OneDrive - GRUPO VERTICE/Escritorio/codigos random/Frases Clave/Csv palabras claves/"
read_conceptos=pd.read_excel(location+"valvoline28nov.xlsx",header=None)


conceptos=list(read_conceptos[0])
n=len(conceptos)



matrixV=np.zeros((n+1,n+1))
i=0
parejas=[]

#%%
for i in range(0,n-1):
    
    x_word=conceptos[i]
    y_word=conceptos[i+1]
       
    parejas.append([x_word,y_word])
        
    print("i",i)
        
print(parejas)
        
#%%

for i in range(0,n-2):
    x_word=conceptos[i]
    y_word=conceptos[i+2]

    parejas.append([x_word,y_word])

#%%

for i in range(0,n-3):
    x_word=conceptos[i]
    y_word=conceptos[i+3]

    parejas.append([x_word,y_word])

#%%

for i in range(0,n-4):
    x_word=conceptos[i]
    y_word=conceptos[i+4]

    parejas.append([x_word,y_word])

#%%
for i in range(0,n-5):
    x_word=conceptos[i]
    y_word=conceptos[i+5]

    parejas.append([x_word,y_word])

#%%

for i in range(0,n-6):
    x_word=conceptos[i]
    y_word=conceptos[i+6]

    parejas.append([x_word,y_word])

#%%
for i in range(0,n-7):
    x_word=conceptos[i]
    y_word=conceptos[i+7]

    parejas.append([x_word,y_word])

#%%
for i in range(0,n-8):
    x_word=conceptos[i]
    y_word=conceptos[i+8]

    parejas.append([x_word,y_word])

#%%
for i in range(0,n-9):
    x_word=conceptos[i]
    y_word=conceptos[i+9]

    parejas.append([x_word,y_word])



#parejas.pop(-1)

#%%Ejemplo mafufo
# Driver code
"""
sentence = ['python coder', 'geeksforgeeks', 'coder in geeksforgeeks','coder para geeksforgeeks','geeksforgeeks es coder']
words = ['coder', 'geeksforgeeks']
"""
#%% Preparar la lista de Oraciones trayendomela de mi dataframe d1

d1=pd.read_excel(location+"youtube-comments636e7f139408e-LUvDfVMHc40.xlsx")


d1=d1.iloc[5:,7:8]

col=["comment"]
d1.columns=col
d1=d1.dropna()
list_sentences=d1['comment'].values.tolist()

#print(check(list_sentences, words))
#lista_parejas=[words,words1]

#%%
d1=pd.DataFrame(concentrador.g)
#list_sentences=d1["g"].values.tolist()
d1=d1.iloc[:,:]


list_sentences=d1["g"].values.tolist()

list_sentences= [str(x) for x in list_sentences]

#%%

for x in list_sentences:
    print("#")
    print(x)

#probar_=["No cuentes los días, haz que los días cuenten. Muhammad Ali","El amor no tiene cura, pero es la cura para todos los males. Leonard Cohen","El mejor momento del día es ahora. Pierre Bonnard","Sé el cambio que quieres ver en el mundo. Mahatma Gandhi","Piensa, sueña, cree y atrévete. Walt Disney","El sentido de la vida es tener valores, no cosas de valor.","Cree que puedes y casi lo habrás logrado. Theodore Roosevelt","Vayas donde vayas, ve con todo tu corazón. Confucio","La mejor forma de predecir el futuro es creándolo. Abraham Lincoln​","Solo imagina lo precioso que puede ser arriesgarse y que todo salga bien. Mario Benedetti","El que tiene un porqué para vivir, puede soportar casi cualquier cómo. Viktor Frankl","Si quieres cambiar el mundo, cámbiate a ti mismo. Mahatma Ghandi","La vida no se trata de encontrarte a ti mismo, sino de crearte a ti mismo. Bernard Shaw","Alguien se sienta en una sombra hoy porque alguien plantó un árbol hace mucho tiempo. Warren Buffet"]

#
#%% Preparar la lista de pares parejas de palabras de un modo bien anticuado pero funciona
#lista_parejas=[['producto','piel'],['suave','piel'],['seca','piel'],['grasa','piel'],['sensible','piel'],['espuma','piel'],['sensación','piel'],['crema','piel'],['recomiendo','piel'],['suave','producto'],['seca','producto'],['grasa','producto'],['sensible','producto'],['espuma','producto'],['sensación','producto'],['crema','producto'],['recomiendo','producto'],['seca','suave'],['grasa','suave'],['sensible','suave'],['espuma','suave'],['sensación','suave'],['crema','suave'],['recomiendo','suave'],['grasa','seca'],['sensible','seca'],['espuma','seca'],['sensación','seca'],['crema','seca'],['recomiendo','seca'],['sensible','grasa'],['espuma','grasa'],['sensación','grasa'],['crema','grasa'],['recomiendo','grasa'],['espuma','sensible'],['sensación','sensible'],['crema','sensible'],['recomiendo','sensible'],['sensación','espuma'],['crema','espuma'],['recomiendo','espuma'],['crema','sensación'],['recomiendo','sensación'],['recomiendo','crema']]
#words=['producto','piel']


#%% Checar que jale la busqueda y guardar en una variable RE de respuestas

print(check(list_sentences, parejas[44]))
re=check(list_sentences, parejas[44])

#%% FUNCION para contar cuantas veces aparecieron juntas las palabras

def numero_de_fc(re):
    #if len(re)==0:
        #print("vacia")
    #else:
        #print("tiene ",len(re))
    return len(re)

#%% REVISAR que sea correcto
print('el conjunto de',parejas[0],numero_de_fc(re),' veces en las que aparecen juntas')

#%% FUNCION PARA APENDEAR resultados

save_pair_together={}

def save_pair(words,re):
    texto=str(words[0])+','+str(words[1])
    
    saved={texto:re}
    save_pair_together.update(saved)
    
    return save_pair_together



save_pair(parejas[0], numero_de_fc(re))
#%%

#FUNCION PARA CAMBIAR DE PAREJA
i=0
for x in parejas:
    
    re=check(list_sentences,x)
    numero_de_fc(re)
    save_pair(x, len(re))
    i+=1
    
#%% cuantas veces aparece cada palabra sola KENJEE


def create_word_count(text_data):
    word_dictionary={}
    for i in text_data:
        if i in word_dictionary.keys():
            word_dictionary[i]+=1
        else:
            word_dictionary[i]=1
    return word_dictionary


stringzote= " ".join(map(str,(comment for comment in concentrador.g)))


str_list = stringzote.split()

words=create_word_count(str_list)

#%% conteo de frecuencia de lista artificial


lista_artificial=conceptos



frequ=[]
for frase in lista_artificial:
    
    frequ.append(stringzote.count(frase))
    
df_artifi = pd.DataFrame(np.column_stack([lista_artificial, frequ]), columns=['phrase', 'freq'])
#dfartifi.to_excel("IGconteofrecuenciasenfrase.xlsx")



#%% para despues sumarla

dict_sum={}
   
for y in parejas:
    
    first=y[0]
    second=y[1]
    ind=df_artifi.index[df_artifi["phrase"]==y[0]][0]
    inds=df_artifi.index[df_artifi["phrase"]==y[1]][0]
    sumF=[df_artifi["freq"].loc[df_artifi["phrase"]==y[0]]][0][ind]
    sumS=[df_artifi["freq"].loc[df_artifi["phrase"]==y[1]]][0][inds]
    
    par_name=first+","+second
    
    dict_sum[par_name]=(int(sumF)+int(sumS))

        
    #print
#print(df_artifi["freq"].where(df_artifi['phrase'] == x))



# =============================================================================
# 
# for x in df_artifi["phrase"]:
# 
#     print(df_artifi["freq"][df_artifi["phrase"]==x])
#     
#     
# =============================================================================
    
    
    
#%% Guardar en un arreglo

d_save=pd.DataFrame.from_dict(save_pair_together.items())
d_sum=pd.DataFrame.from_dict(dict_sum.items())

d_save.columns=["frase","valor"]
d_sum.columns=["frase","suma"]
d_total= pd.merge(d_save, d_sum, on="frase")

# =============================================================================
# 
# Z=dict(save_pair_together,dict_sum)
# Z1=save_pair_together|dict_sum
# 
# =============================================================================
    
d_total["pormilaje"]=(d_total["valor"]/d_total["suma"])*1000
d_total.to_excel("correlaciondepalabras.xlsx")
    







#%% Exportar diccionario como dataframe

frameSalvado=pd.DataFrame(save_pair_together.items())

#frameSalvado.to_csv("datosSalvadosparaMatriz.csv")
    
 
    
#%% Nuevo reto: construir un heatmap para correlaciones

import seaborn as sns
import matplotlib.pyplot as plt

correl=pd.read_excel("motortabla.xlsx",index_col=("PALABRA"))
#correl.set_index("PALABRA")
correl=correl/100

plt.figure(figsize=(20,8))
sns.heatmap(correl, vmax=1, vmin=-1, center=0,
			linewidth=.5,square=True, annot = True,
            annot_kws = {'size':8},fmt='.1f', cmap='BrBG_r',   # ax: use this when using subplot
            cbar_kws = dict(use_gridspec=False,location="top", shrink=0.9)) # cbar_kws: for positioning cbar and "shrink" for reducing cbar size
plt.title('Correlation')
plt.show()


# =============================================================================
# df = {
#   "Array_1": [30, 70, 100],
#   "Array_2": [65.1, 49.50, 30.7]
# }
#  
# data = pd.DataFrame(df)
#  
# =============================================================================
# =============================================================================
# nose=data.corr()
# =============================================================================




#%% ARREGLO

A= np.zeros((n,n))

A[0][1]=d_total["pormilaje"][0]
A[1][2]=d_total["pormilaje"][1]
A[2][3]=d_total["pormilaje"][2]
A[3][4]=d_total["pormilaje"][3]
A[4][5]=d_total["pormilaje"][4]
A[5][6]=d_total["pormilaje"][5]
A[6][7]=d_total["pormilaje"][6]
A[7][8]=d_total["pormilaje"][7]
A[8][9]=d_total["pormilaje"][8]




A[0][2]=d_total["pormilaje"][9]
A[1][3]=d_total["pormilaje"][10]
A[2][4]=d_total["pormilaje"][11]
A[3][5]=d_total["pormilaje"][12]
A[4][6]=d_total["pormilaje"][13]
A[5][7]=d_total["pormilaje"][14]
A[6][8]=d_total["pormilaje"][15]
A[7][9]=d_total["pormilaje"][16]



A[0][3]=d_total["pormilaje"][17]
A[1][4]=d_total["pormilaje"][18]
A[2][5]=d_total["pormilaje"][19]
A[3][6]=d_total["pormilaje"][20]
A[4][7]=d_total["pormilaje"][21]
A[5][8]=d_total["pormilaje"][22]
A[6][9]=d_total["pormilaje"][23]



A[0][4]=d_total["pormilaje"][24]
A[1][5]=d_total["pormilaje"][25]
A[2][6]=d_total["pormilaje"][26]
A[3][7]=d_total["pormilaje"][27]
A[4][8]=d_total["pormilaje"][28]
A[5][9]=d_total["pormilaje"][29]




A[0][5]=d_total["pormilaje"][30]
A[1][6]=d_total["pormilaje"][31]
A[2][7]=d_total["pormilaje"][32]
A[3][8]=d_total["pormilaje"][33]
A[4][9]=d_total["pormilaje"][34]



A[0][6]=d_total["pormilaje"][35]
A[1][7]=d_total["pormilaje"][36]
A[2][8]=d_total["pormilaje"][37]
A[3][9]=d_total["pormilaje"][38]


A[0][7]=d_total["pormilaje"][39]
A[1][8]=d_total["pormilaje"][40]
A[2][9]=d_total["pormilaje"][41]



A[0][8]=d_total["pormilaje"][42]
A[1][9]=d_total["pormilaje"][43]


A[0][9]=d_total["pormilaje"][44]
#%% LA OTRA PARTE DEL TRIANGULO


A[1][0]=d_total["pormilaje"][0]
A[2][1]=d_total["pormilaje"][1]
A[3][2]=d_total["pormilaje"][2]
A[4][3]=d_total["pormilaje"][3]
A[5][4]=d_total["pormilaje"][4]
A[6][5]=d_total["pormilaje"][5]
A[7][6]=d_total["pormilaje"][6]
A[8][7]=d_total["pormilaje"][7]
A[9][8]=d_total["pormilaje"][8]




A[2][0]=d_total["pormilaje"][9]
A[3][1]=d_total["pormilaje"][10]
A[4][2]=d_total["pormilaje"][11]
A[5][3]=d_total["pormilaje"][12]
A[6][4]=d_total["pormilaje"][13]
A[7][5]=d_total["pormilaje"][14]
A[8][6]=d_total["pormilaje"][15]
A[9][7]=d_total["pormilaje"][16]



A[3][0]=d_total["pormilaje"][17]
A[4][1]=d_total["pormilaje"][18]
A[5][2]=d_total["pormilaje"][19]
A[6][3]=d_total["pormilaje"][20]
A[7][4]=d_total["pormilaje"][21]
A[8][5]=d_total["pormilaje"][22]
A[9][6]=d_total["pormilaje"][23]



A[4][0]=d_total["pormilaje"][24]
A[5][1]=d_total["pormilaje"][25]
A[6][2]=d_total["pormilaje"][26]
A[7][3]=d_total["pormilaje"][27]
A[8][4]=d_total["pormilaje"][28]
A[9][5]=d_total["pormilaje"][29]




A[5][0]=d_total["pormilaje"][30]
A[6][1]=d_total["pormilaje"][31]
A[7][2]=d_total["pormilaje"][32]
A[8][3]=d_total["pormilaje"][33]
A[9][4]=d_total["pormilaje"][34]



A[6][0]=d_total["pormilaje"][35]
A[7][1]=d_total["pormilaje"][36]
A[8][2]=d_total["pormilaje"][37]
A[9][3]=d_total["pormilaje"][38]


A[7][0]=d_total["pormilaje"][39]
A[8][1]=d_total["pormilaje"][40]
A[9][2]=d_total["pormilaje"][41]



A[8][0]=d_total["pormilaje"][42]
A[9][1]=d_total["pormilaje"][43]


A[9][0]=d_total["pormilaje"][44]

#%%






#%% Opcion 2


# Python3 program to Check if given words
# appear together in a list of sentence

def check(sentence, words):
	res = []
	for substring in sentence:
		k = [ w for w in words if w in substring ]
		if (len(k) == len(words) ):
			res.append(substring)
			
	return res
	
# Driver code
sentence = ['python coder', 'geeksforgeeks', 'coder in geeksforgeeks']
words = ['coder', 'geeksforgeeks']
print(check(sentence, words))
