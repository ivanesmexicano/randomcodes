# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:04:37 2022

@author: Ivan Tonatiuh
"""

import requests

import facebook

#%%
token= "EAAHaXHw7fS8BAPOOSbzfb9yHAFiDVbd3xXU4ZBhmqGMLYsXFkcb83zQK6sJE8Yet9ZASdzfB1uCyu4j2kBxZBzbfl9R7FLjv2eZAzP7Nkbp2snegXogm1LzHFu7zNlZBBq74RXqWXdEZBUicwOOQPvmh6YRF4LuOXRoRjVEN2LNt7yctYl5z2sUBR3lXJQbYYm89TddxXUKde7kkZBTEtsU"


graph = facebook.GraphAPI(access_token=token) # Initializing the object

profile = graph.get_object("me") # Extracting your own profile

#graph.put_object("me", "feed", message="Posting on my wall!")

#%%

a= graph.request("103492478186347")




# =============================================================================
# curl -i -X GET \
#  "https://graph.facebook.com/v15.0/me?fields=id%2Cname&access_token=EAAHaXHw7fS8BAPOOSbzfb9yHAFiDVbd3xXU4ZBhmqGMLYsXFkcb83zQK6sJE8Yet9ZASdzfB1uCyu4j2kBxZBzbfl9R7FLjv2eZAzP7Nkbp2snegXogm1LzHFu7zNlZBBq74RXqWXdEZBUicwOOQPvmh6YRF4LuOXRoRjVEN2LNt7yctYl5z2sUBR3lXJQbYYm89TddxXUKde7kkZBTEtsU"
# =============================================================================


#%%

b=graph.request("103492478186347?fields=fan_count,followers_count")
