import pandas as pd
import geopandas as gpd
import sys
from shapely.geometry import Point,Polygon
# read three csv satellites dataset into python
read_MODIS = pd.read_csv("C:\\Python\\airshelter\\get_data\\MODIS_C6_Australia_NewZealand_24h.csv")
read_SUOMI_VIIR = pd.read_csv("C:\\Python\\airshelter\\get_data\\SUOMI_VIIRS_C2_Australia_NewZealand_24h.csv")
read_J1_VIIR = pd.read_csv("C:\\Python\\airshelter\\get_data\\J1_VIIRS_C2_Australia_NewZealand_24h.csv")
# add one column use to save source
read_MODIS["source"] = "MODIS"
read_SUOMI_VIIR["source"] = "SUOMI VIIR"
read_J1_VIIR["source"]="J1 VIIR"
# combine three dataset together
seven_day_fire = pd.concat([read_MODIS, read_SUOMI_VIIR,read_J1_VIIR])
seven_day_fire = seven_day_fire.reset_index()
del seven_day_fire["index"]
# read vic shapefile use to filter the bushfire happens in Victoria
victoria_map = gpd.read_file("C:\\Python\\airshelter\\get_data\\VIC_STATE_POLYGON_shp")
vic_seven_day_fire_list = columns=seven_day_fire.columns.tolist()
vic_seven_day_fire = pd.DataFrame(columns=vic_seven_day_fire_list)
for i in range(0,len(seven_day_fire)):
    point = Point(seven_day_fire.loc[i,"longitude"],seven_day_fire.loc[i,"latitude"])
    # judgment the camping site point within the bush fire area
    records = victoria_map.geometry.contains(point)
    if pd.Series(records).any() == True:
        vic_seven_day_fire=vic_seven_day_fire.append(pd.Series(seven_day_fire.loc[i].tolist(), index=vic_seven_day_fire_list),ignore_index=True)
# save it into your path
vic_seven_day_fire.to_csv("C:\\Python\\airshelter\\reformat_data\\vic_fire_data.csv", index=False)
sys.exit()