#This will be a lambda function later on
#@Author: Benjamin Johnson
import json
import requests
from bs4 import BeautifulSoup
import re
import time

def scrape(event, context):
    #C%23='C#', C+2B%2B='C++', 
    terms={"GIS":"GIS","GIS+Python":"GIS Python","GIS+Java":"GIS Java", "GIS+SQL":"GIS SQL", 
        "GIS+Ruby":"GIS Ruby", "GIS+Javascript":"GIS Javascript","GIS+HTML":"GIS HTML",
        "GIS+CSS":"GIS CSS", "GIS+C":"GIS C", "GIS+C%23":"GIS C#", "GIS+C%2B%2B":"GIS C++",
        "GIS+BASH":"GIS Bash", "GIS+SHELL":"GIS Shell", "GIS+UNIX":"GIS Unix",
        "GIS+PHP":"GIS PHP", "GIS+typescript":"GIS Typescript","GIS+SWIFT":"GIS Swift",
        "GIS+OBJECTIVE+C":"GIS Objective C", "GIS+.NET":"GIS .Net", "GIS+MATLAB":"GIS MATLAB",
        "GIS+DELPHI":"GIS Delphi","GIS+MAPBOX":"GIS MapBox", "GIS+ARCGIS":"GIS ArcGIS",
        "GIS+QGIS":"GIS QGIS", "GIS+LEAFLET":"GIS Leaflet", "GIS+PostgreSQL":"GIS PostgreSQL", 
        "GIS+SQL+SERVER":"GIS SQL Server", "GIS+ORACLE":"GIS Oracle", "GIS+NOSQL":"GIS NoSQL",
        "GIS+MONGODB":"GIS MongoDB", "GIS+Cassandra":"GIS Cassandra","GIS+REDIS":"GIS Redis",
        "GIS+HBASE":"GIS HBASE", "GIS+DYNAMODB":"GIS DynamoDB", "GIS+AWS":"GIS AWS",
        "GIS+HADOOP":"GIS HADOOP", "GIS+AutoCAD":"GIS AutoCAD","GIS+CIVIL3D":"GIS Civil3D",
        "GIS+VBA":"GIS VBA", "GIS+ERDAS+IMAGINE":"GIS ERDAS IMAGINE", "GIS+ENVI":"GIS ENVI",
        "GIS+GDAL":"GIS GDAL", "GIS+CAD":"GIS CAD"}
    jobs=[]
    for key, value in terms.items():  
        page = requests.get("https://www.indeed.com/jobs?q="+key) 
        soup = BeautifulSoup(page.content, 'html.parser')
        time.sleep(2)
        n_jobs = 0
        for meta in soup.find_all('meta', attrs={"name": "description"}):
            n_jobs = re.search('\d+', meta["content"].replace(',','')).group(0)
        scrape_info={
        'input' : event,
        'status_code' : page.status_code,
        'search term' : value,
        'number of jobs' : n_jobs,
        'date' : time.strftime("%d_%m_%Y")
        }
        jobs.append(scrape_info)

    ## dd/mm/yyyy format
    time_stamp=time.strftime("%d_%m_%Y")
    with open('/Users/benjohnson/Desktop/Indeed_scraped/'+'GIS_'+time_stamp+'.txt', 'w') as outfile:
        json.dump(jobs, outfile)

scrape(None,None)
