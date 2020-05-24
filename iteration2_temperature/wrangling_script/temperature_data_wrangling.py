import pandas as pd
import os
import re
from datetime import datetime
# due to lack of information of monitoring station 
#the only method is check the website and record station information by ourself
temperature_station_dic = {26021:[-37.75,140.77,"Mount Gambier"],78015:[-36.31,141.65,"Nhill"],76031:[-34.24,142.09,"Mildura"],90015:[-38.86,143.51,"Cape Otway"],80023:[-35.72,143.92,"Kerang"],87031:[-37.86,144.76,"Laverton"],86338:[-37.83,144.98 ,"Melbourne"],74258:[-35.56,144.95 ,"Deniliquin"],85096:[-39.13,146.42,"Wilsons Promontory"],82039:[-36.1,146.51,"Rutherglen"],85072:[-38.12,147.13,"Sale"],84145:[-37.69,148.47,"Orbost"],72161:[-35.94,148.38,"Cabramurra"], 84016:[-37.57,149.92,"Gabo Island"]}
# setting the data path
dir_path = "E:\\notebooks\\IE-Project\\temperature_data"
station_keys = temperature_station_dic.keys()
# Because of the huge amount of data, it takes about 8 hours to process at the same time.
# here I deal with each monitoring station separately, and all stations are the same except for different Numbers
# create dataframe to store new data for 78015 station
temp_78015_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    # Find the 78015 station data from all station files
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 78015:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            # Extract the number of the monitoring station and the recorded date from the first column
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            # get latitude, longitude, station name, max temperature and min temperature from other columns
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            # handling missing value
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            # add it into new dataframe
            temp_78015_df.loc[len(temp_78015_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
# restore it in new file
temp_78015_df.to_csv("temp_78015_df.csv")
# handling 76031 mornitoring station
temp_76031_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 76031:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_76031_df.loc[len(temp_76031_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_76031_df.to_csv("temp_76031_df.csv")
# handling 90015 mornitoring station
temp_90015_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 90015:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_90015_df.loc[len(temp_90015_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_90015_df.to_csv("temp_90015_df.csv")
# handling 80023 mornitoring station
temp_80023_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 80023:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_80023_df.loc[len(temp_80023_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_80023_df.to_csv("temp_80023_df.csv")
# handling 87031 mornitoring station
temp_87031_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 87031:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_87031_df.loc[len(temp_87031_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_87031_df.to_csv("temp_87031_df.csv")
# handling 86338 mornitoring station
temp_86338_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 86338:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_86338_df.loc[len(temp_86338_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_86338_df.to_csv("temp_86338_df.csv")
# handling 74258 mornitoring station
temp_74258_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 74258:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_74258_df.loc[len(temp_74258_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_74258_df.to_csv("temp_74258_df.csv")
# handling 85096 mornitoring station
temp_85096_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 85096:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_85096_df.loc[len(temp_85096_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_85096_df.to_csv("temp_85096_df.csv")
# handling 82039 mornitoring station
temp_82039_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 82039:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_82039_df.loc[len(temp_82039_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_82039_df.to_csv("temp_82039_df.csv")
# handling 85072 mornitoring station
temp_85072_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 85072:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_85072_df.loc[len(temp_85072_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_85072_df.to_csv("temp_85072_df.csv")
# handling 84145 mornitoring station
temp_84145_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 84145:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_84145_df.loc[len(temp_84145_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_84145_df.to_csv("temp_84145_df.csv")
# handling 72161 mornitoring station
temp_72161_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 72161:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_72161_df.loc[len(temp_72161_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_72161_df.to_csv("temp_72161_df.csv")
# handling 84016 mornitoring station
temp_84016_df = pd.DataFrame(columns=["station_code","date","lat","lng","station_name","max_temp","min_temp"])
for file in os.listdir(dir_path):
    station_name = re.search(r"hqnew0(.*)", file)
    if int(station_name[1]) == 84016:
        file_name = dir_path + "\\" + file
        content = pd.read_csv(file_name,header=None,sep='\s+')
        for i in range(0,len(content)):
            split_numbers = re.search(r"(^\d{5})(\d.*)", str(content.loc[i,0]))
            station_code = split_numbers[1]
            date = datetime.strptime(split_numbers[2],'%Y%m%d')
            lat = temperature_station_dic[int(station_name[1])][0]
            lng = temperature_station_dic[int(station_name[1])][1]
            name = temperature_station_dic[int(station_name[1])][2]
            max_temp = str(content.loc[i,1]/10)
            min_temp = str(content.loc[i,2]/10)
            if max_temp == "-99.9":
                max_temp = "Na"
            if min_temp == "-99.9":
                min_temp = "Na"
            temp_84016_df.loc[len(temp_84016_df)]=[station_code,date,lat,lng,name,max_temp,min_temp]
temp_84016_df.to_csv("temp_84016_df.csv")