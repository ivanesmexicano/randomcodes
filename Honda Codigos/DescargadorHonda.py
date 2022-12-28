# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 09:33:11 2022

@author: Ivan Tonatiuh
"""

# import packages
from apiclient.discovery import build
from google.oauth2.service_account import Credentials
import pandas as pd
# Locate the json key file generated in the previous step
KEY_FILE_LOCATION = r'C:/Users/Ivan Tonatiuh/OneDrive - GRUPO VERTICE/Escritorio/codigos random/Honda Codigos/proyectname-descargarrephonda-457d9ad043eb.json'
# Build Analytics Reporting API V4 service object.    
def get_service():
    SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
    credentials = Credentials.from_service_account_file(
        KEY_FILE_LOCATION, scopes=SCOPES
    )
    service = build(serviceName='analyticsreporting', version='v4', credentials=credentials)
    return service

#%%

def get_report(
    service, view_id, 
    #default date range 
    start_date='7daysAgo', end_date='yesterday', 
    metrics=[], dimensions=[]
    ):
    return service.reports().batchGet(
            body={
                'reportRequests': [{
                    'viewId': view_id,
                    'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
                    'metrics': [{'expression': m} for m in metrics],
                    'dimensions': [{'name': d} for d in dimensions],
                }]
            }).execute()
# Parameter to get report
VIEW_ID = '88424329'  ## <-- input your GA view id
metrics = ['ga:totalEvents'] ## <-- input the metrics & dimensions
dimensions = ['ga:deviceCategory','ga:eventAction']

#dimensions = ['ga:source', 'ga:medium']
start_date, end_date = '2022-11-03', '2022-11-10' ##<--input timeframe
service = get_service()
response = get_report(
                service, VIEW_ID,
                start_date, end_date,
                metrics, dimensions
                )


#ga:percentNewSessions,% New Sessions

#%%


def res_to_df(res):
    report = res['reports'][0]
    dimensions = report['columnHeader']['dimensions']
    metrics = [m['name'] for m in report['columnHeader']['metricHeader']['metricHeaderEntries']]
    headers = [*dimensions, *metrics]
    
    data_rows = report['data']['rows']
    data = []
    for row in data_rows:
        data.append([*row['dimensions'], *row['metrics'][0]['values']])
    
    return pd.DataFrame(data=data, columns=headers)
    
df = res_to_df(response)

#df.to_csv("df0.csv")
