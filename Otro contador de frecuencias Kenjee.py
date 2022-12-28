# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:16:23 2022

@author: Ivan Tonatiuh
"""

def create_word_count(text_data):
    word_dictionary={}
    for i in text_data:
        if i in word_dictionary.keys():
            word_dictionary[i]+=1
        else:
            word_dictionary[i]=1
    return word_dictionary
    
video_data=["aceite","motor","coche","sintético","aceite","profesional"]

words=create_word_count(video_data)

