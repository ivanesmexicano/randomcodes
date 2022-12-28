# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:01:46 2022

@author: Ivan Tonatiuh
"""

import pandas as pd

dataset=pd.read_csv("reviewsHellaOil.csv",encoding="utf-8")

dataset.to_excel("frasesHellaOil.xlsx")
