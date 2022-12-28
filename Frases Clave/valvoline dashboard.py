# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:04:37 2022

@author: Ivan Tonatiuh
"""

import requests

import facebook

#%%
token= "EAAP2CdySPZAkBACoowt1OVhrJ4Lxl1D1ZAT6ULOQo1YdsUIvaVggp0oWD4ZB2eq6uJinkiGBXz2u6ME0npglJJZB7Aqt67ip7QR2o9hUZA0SfPEPIv1ZBruccLXgZB5LE4sd7RHJsdgZAv54fGJWck8l01xT6pk6IEqJVRxZB1Y1qRh0OjqI0IkhL"

pagetoken="EAAP2CdySPZAkBACoowt1OVhrJ4Lxl1D1ZAT6ULOQo1YdsUIvaVggp0oWD4ZB2eq6uJinkiGBXz2u6ME0npglJJZB7Aqt67ip7QR2o9hUZA0SfPEPIv1ZBruccLXgZB5LE4sd7RHJsdgZAv54fGJWck8l01xT6pk6IEqJVRxZB1Y1qRh0OjqI0IkhL"
graph = facebook.GraphAPI(access_token=token) # Initializing the object

profile = graph.get_object("me") # Extracting your own profile

#graph.put_object("me", "feed", message="Posting on my wall!")

#%%valvoline page id 1679451712349568


a= graph.request("1679451712349568")




# =============================================================================
# curl -i -X GET \
#  "https://graph.facebook.com/v15.0/me?fields=id%2Cname&access_token=EAAHaXHw7fS8BAPOOSbzfb9yHAFiDVbd3xXU4ZBhmqGMLYsXFkcb83zQK6sJE8Yet9ZASdzfB1uCyu4j2kBxZBzbfl9R7FLjv2eZAzP7Nkbp2snegXogm1LzHFu7zNlZBBq74RXqWXdEZBUicwOOQPvmh6YRF4LuOXRoRjVEN2LNt7yctYl5z2sUBR3lXJQbYYm89TddxXUKde7kkZBTEtsU"
# =============================================================================


#%%

b=graph.request("103492478186347?fields=fan_count,followers_count")

#%%
#engagement
#page_impressions_unique

#identificador facebook app valvoline 1114947145842073
#clave secreta app valvoline 71974dd24846516a521ff217d6e334f2

c=graph.request("103492478186347/insights/page_engaged_users&access_token=token")






#%% bearer de usuario 
{
    "access_token": "EAAP2CdySPZAkBANg8oeIZAeGDiK3GGbjFA15rHrRS2OxYyQH9R7yyGVX9Rzv2ZBmVWKFtr70cmvDsAS5G4nkMHVrOVJeZCGuI2InRolXNR9tZBBdFUsDqT9x017fA3nkvqBSYe9bxFA6XZAZAVaDI0JkmCqb3ZA91tpUvjt1JSh8YwZDZD",
    "token_type": "bearer",
    "expires_in": 5184000
}
    
    #%% incaducable token de acceso a la pagina zambos
    
   {
    "access_token": "EAAP2CdySPZAkBACoowt1OVhrJ4Lxl1D1ZAT6ULOQo1YdsUIvaVggp0oWD4ZB2eq6uJinkiGBXz2u6ME0npglJJZB7Aqt67ip7QR2o9hUZA0SfPEPIv1ZBruccLXgZB5LE4sd7RHJsdgZAv54fGJWck8l01xT6pk6IEqJVRxZB1Y1qRh0OjqI0IkhL",
    "id": "1679451712349568"
}