# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:02:26 2022

@author: Ivan Tonatiuh
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection


def nested_circles(data, labels=None, c=None, ax=None, 
                   cmap=None, norm=None, textkw={}):
    ax = ax or plt.gca()
    data = np.array(data)
    R = np.sqrt(data/data.max())
    p = [plt.Circle((0,r), radius=r) for r in R[::-1]]
    arr = data[::-1] if c is None else np.array(c[::-1])
    col = PatchCollection(p, cmap=cmap, norm=norm, array=arr)

    ax.add_collection(col)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.autoscale()

    if labels is not None:
        kw = dict(color="white", va="center", ha="center")
        kw.update(textkw)
        ax.text(0, R[0], labels[0], **kw)
        for i in range(1, len(R)):
            ax.text(0, R[i]+R[i-1], labels[i], **kw)
    return col

#%% APLICAR VALORES EN DATA

data = [1,3,4,5,6]
labels = list("ABCDE")
nested_circles(data, labels=labels, cmap="copper", textkw=dict(fontsize=14))
plt.show()


#%% COLORES RAROS

data = [1,3,4,5,6]
labels = list("ABCDE")
codes = [5,3,1,4,2]
circles = nested_circles(data, labels=labels, c=codes, cmap="plasma", 
                         textkw=dict(color="black", fontsize=14))
plt.colorbar(circles, label="Codes")
plt.title("Diagram")
plt.show()


#%% Modificaciones de Iván

rubros=["VSJ","S. Hidalgo","Gdl","Jalisco","México"]
data = [100,300,400,500,600]
labels = rubros
nested_circles(data, labels=labels, cmap="plasma", textkw=dict(fontsize=14))
plt.show()

#%%

