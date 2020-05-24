import pandas as pd
import numpy as np
import datetime
import math
import os
from geopy.distance import geodesic
# create new data frame for store data
temp_monthly_df = pd.DataFrame(columns=["station_code","month","lat","lng","station_name","avg_max_temp","avg_min_temp"])
dir_path = "seperata_temp_data"
for file in os.listdir(dir_path):
        file_name = dir_path + "\\" + file
        temp_data = pd.read_csv(file_name)
        # create two columns to store month and year
        temp_data['month'] = pd.DatetimeIndex(temp_data['date']).month
        temp_data['year'] = pd.DatetimeIndex(temp_data['date']).year
        for i in range(1,13):
        	# get max and min data in each month
            temp_max_monthly = temp_data[(temp_data['month']==i) & (temp_data['max_temp']!="Na")]
            temp_max_monthly = temp_max_monthly.astype({'max_temp': 'float'})
            temp_min_monthly = temp_data[(temp_data['month']==i) & (temp_data['min_temp']!="Na")]
            temp_min_monthly = temp_min_monthly.astype({'min_temp': 'float'})    
            # calculate the mean value of temperature
            avg_max_temp = round(temp_max_monthly["max_temp"].mean())
            avg_min_temp = round(temp_min_monthly["min_temp"].mean())
            # otehr features
            station_code = temp_data["station_code"][i]
            month = i
            lat = temp_data["lat"][i]
            lng = temp_data["lng"][i]
            station_name = temp_data["station_name"][i]
            # add all variables to new data frame
            temp_monthly_df.loc[len(temp_monthly_df)]=[station_code,month,lat,lng,station_name,avg_max_temp,avg_min_temp]
# setting attractions latitude and longitude 
place_latlng={"-37.999183, 147.640562":"Gippsland lakes","-37.863799, 144.973203":"St kilda","-37.916325, 144.986495":"Brighton Beach", "-37.210955, 142.397560":"Grampians", "-37.834896, 145.347100":"Dandenong ranges", "-37.810858, 144.965682":"Main Melbourne", "-37.233926, 146.436825":"Mount Buller", "-38.680614, 143.391629":"Greate Ocean Road", "-37.564166, 143.850335":"Ballarat", "-38.490383, 145.206726":"Phillip Island", "-37.816410, 144.898382":"Yarra Valley", "-38.374795, 144.981905":"Shire of Mornington Peninsula", "-37.342267, 144.149260":"Daylesford", "-36.147063, 144.753529":"The Murry"}
# create new columns to store final data
final_data = pd.DataFrame(columns=[])
sta_lat_list = list(temp_monthly_df["lat"].drop_duplicates())
sta_lng_list = list(temp_monthly_df["lng"].drop_duplicates())
# for each attraction, find the nearest monitoring station and return the value of it
for i in place_latlng.keys():
    latlng = i.split(",")
    rel_lat = 0
    rel_lng = 0
    distance = 99999999999999999999999
    for j in range(0,len(sta_lat_list)):
        dist = geodesic((sta_lat_list[j],sta_lng_list[j]), (latlng[0],latlng[1])).km
        if dist < distance:
            distance = dist
            rel_lat = sta_lat_list[j]
            rel_lng = sta_lng_list[j]
    temp_monthly_place_df = temp_monthly_df[(temp_monthly_df["lat"]==rel_lat)&(temp_monthly_df["lng"]==rel_lng)]
    temp_monthly_place_df["place"] = place_latlng[i]
    final_data = pd.concat([final_data,temp_monthly_place_df])
final_data.to_csv("place_temperature_dataset.csv", index=False)