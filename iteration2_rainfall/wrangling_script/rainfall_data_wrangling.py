import pandas as pd
import os
import re
import geopandas as gpd
from shapely.geometry import Point,Polygon
from datetime import datetime
from geopy.distance import geodesic
import datetime
# read data and Victoria region shapefile in python
station_info = pd.read_table("rainfall_data\HQMR_stations.txt",sep="\s+", header=None)
victoria_map = gpd.read_file("E:\\Study\\20 semester 1\\Project\\bushfire\\victoria\\VIC_STATE_POLYGON_shp")
rainfall_station_dic={}
# for each monitoring station, judgment the camping site point within the bush fire area
for i in range(0,len(station_info)):
    # convert latitude and longitude into point
    point = Point(station_info.loc[i,2],station_info.loc[i,1])
    # judgment the camping site point within the bush fire area
    records = victoria_map.geometry.contains(point)
    if pd.Series(records).any() == True:
        rainfall_station_dic[station_info.loc[i,0]] = [station_info.loc[i,1],station_info.loc[i,2]]
# create attraction coordinates according to the position
place_latlng={"-37.999183, 147.640562":"Gippsland lakes","-37.863799, 144.973203":"St kilda","-37.916325, 144.986495":"Brighton Beach", "-37.210955, 142.397560":"Grampians", "-37.834896, 145.347100":"Dandenong ranges", "-37.810858, 144.965682":"Main Melbourne", "-37.233926, 146.436825":"Mount Buller", "-38.680614, 143.391629":"Greate Ocean Road", "-37.564166, 143.850335":"Ballarat", "-38.490383, 145.206726":"Phillip Island", "-37.816410, 144.898382":"Yarra Valley", "-38.374795, 144.981905":"Shire of Mornington Peninsula", "-37.342267, 144.149260":"Daylesford", "-36.147063, 144.753529":"The Murry"}
nearest_place = pd.DataFrame(columns=[])
sta_lat_list = list(i[0] for i in rainfall_station_dic.values())
sta_lng_list = list(i[1] for i in rainfall_station_dic.values())
count = 0
# for each attraction, get the nearest monitoring station data
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
    station_num = 0
    for key, value in rainfall_station_dic.items():
        if value == [rel_lat,rel_lng]:
            station_num = key
    # create two dataset to store the information of rainfall station, attraction name
    temp_df = pd.DataFrame(columns=[])
    temp_df.loc[count,"rainfall_station"] = station_num
    temp_df.loc[count,"attraction"] = place_latlng[i]
    nearest_place = pd.concat([nearest_place,temp_df])
    count +=1
# read data from local and get the rainfall data from monitoring station that nearest attraction
dir_path = "E:\\notebooks\\IE-Project\\rainfall_data"
rainfall_df = pd.DataFrame(columns=[])
for i in range(0,len(nearest_place)):
    station = "0"+str(int(nearest_place.loc[i,"rainfall_station"]))
    for file in os.listdir(dir_path):
        station_name = re.search(r"prcphq.(.*).month", file)
        if station_name == None:
            pass
        else:
            if station_name[1] == station:
                file_name = dir_path + "\\" + file
                content = pd.read_csv(file_name,sep='\s+')
                # rename columns for convenient
                content.rename(columns={list(content)[0]:'date',list(content)[2]:'rainfall_vol'}, inplace=True)
                # extract month from date and input in new colunm "month"
                content["month"] = pd.DatetimeIndex(pd.to_datetime(content["date"], format="%Y%m%d")).month
    # for each month, calculate the average rainfall
    for j in range(1,13):
        avg_rainfall = content[(content["month"]==j) & (content["rainfall_vol"]!=99999.9)]["rainfall_vol"].mean()
        rainfall_temp_df = pd.DataFrame(columns=[])
        rainfall_temp_df.loc[j-1,"attraction"] = nearest_place.loc[i,"attraction"]
        rainfall_temp_df.loc[j-1,"rainfall_station"] = nearest_place.loc[i,"rainfall_station"]
        rainfall_temp_df.loc[j-1,"month"] = int(j)
        rainfall_temp_df.loc[j-1,"avg_rainfall"] = avg_rainfall
        rainfall_df = pd.concat([rainfall_df,rainfall_temp_df])           
rainfall_df.to_csv("place_rainfall_dataset")  