import urllib, urllib3, sys
import certifi 
import pandas as pd
import re
import time
# read camping site file
read_camping_site = pd.read_csv("C:\\Python\\airshelter\\get_data\\recweb_site.csv")
all_lat = read_camping_site["LATITUDE"]
all_lng = read_camping_site["LONGITUDE"]
# create three columns to store AQI information
read_camping_site["AQI_num"]="no data"
read_camping_site["AQI"]="no data"
read_camping_site["Suggestion"]="no data"
# search air quality data, find pm25 and pm10 and aqi from it
def searchairq(air_quality_data):
    air_quality = str(air_quality_data)
    pm25 = re.search(r"pm25\":{\"v\":(.*?)}", air_quality)
    pm10 = re.search(r"pm10\":{\"v\":(.*?)}", air_quality)
    aqi = re.search(r"\"aqi\":(.*?),", air_quality)
    try:
        return aqi[1]
    except:
        return "no data"
#set api methods
host = 'https://api.waqi.info'
method = 'GET'
appcode='token=35b4c6629577904042044bbe7863d27097b18234'
# using api get data according to coordinates
for i in range(0,len(all_lng)):
    path = '/feed/geo:'+str(all_lat[i])+';'+str(all_lng[i])+'/'
    url = host+path+'?'+appcode
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    request = http.request(method, url)
    print(request.data)
    pm_data = int(searchairq(request.data))
    # setting the sugeestion based on the AQI value, add AQI and suggestion to camping site dataset
    if pm_data>=0 and pm_data<=50:
        read_camping_site.loc[i,"AQI_num"] = pm_data
        read_camping_site.loc[i,"AQI"] = "Good"
        read_camping_site.loc[i,"Suggestion"] = "Air quality is satisfactory, and air pollution poses little or no risk."
    elif pm_data >=51 and pm_data<=100:
        read_camping_site.loc[i,"AQI_num"] = pm_data
        read_camping_site.loc[i,"AQI"] = "Moderate"
        read_camping_site.loc[i,"Suggestion"] = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
    elif pm_data >=101 and pm_data<=150:
        read_camping_site.loc[i,"AQI_num"] = pm_data
        read_camping_site.loc[i,"AQI"] = "Unhealthy for Sensitive Groups"
        read_camping_site.loc[i,"Suggestion"] = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
    elif pm_data >=151 and pm_data<=200:
        read_camping_site.loc[i,"AQI_num"] = pm_data
        read_camping_site.loc[i,"AQI"] = "Unhealthy"
        read_camping_site.loc[i,"Suggestion"] = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
    elif pm_data >=201 and pm_data<=300:   
        read_camping_site.loc[i,"AQI_num"] = pm_data
        read_camping_site.loc[i,"AQI"] = "Very Unhealthy"
        read_camping_site.loc[i,"Suggestion"] = "Health alert: The risk of health effects is increased for everyone."
    elif pm_data >=301: 
        read_camping_site.loc[i,"AQI_num"] = pm_data
        read_camping_site.loc[i,"AQI"] = "Hazardous"
        read_camping_site.loc[i,"Suggestion"] = "Health warning of emergency conditions: everyone is more likely to be affected."
    else:
        read_camping_site.loc[i,"AQI_num"] = "no data"
        read_camping_site.loc[i,"AQI"] = "no data"
        read_camping_site.loc[i,"Suggestion"] = "no data"
read_camping_site.to_csv("C:\\Python\\airshelter\\reformat_data\\recweb_site_with_air_quality.csv",index=False)
sys.exit()