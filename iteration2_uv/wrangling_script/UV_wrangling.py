import pandas as pd
import datetime
# read data
uv_data = pd.read_csv("uv_data\\uv.csv")
# filter data which is less than 0.01
uv_data_filter_1 = uv_data[uv_data["UV_Index"]>0.01]
# add two columns to store month and day
uv_data_filter_1["month"] = pd.DatetimeIndex(uv_data_filter_1["Date-Time"]).month
uv_data_filter_1["day"] = pd.DatetimeIndex(uv_data_filter_1["Date-Time"]).day
# create new data frame to store data
final_data = pd.DataFrame(columns=[])
# calculate mean and max value in each data in different month
for i in range(1,13):
    # Since each month has different days, the data is processed according to different months
    if i in [1,3,5,7,8,10,12]:
        uv_temp_df = pd.DataFrame(columns=[])
        for j in range(1,31):
            # calcuate mean uv in each day
            day_mean = uv_data_filter_1[(uv_data_filter_1["month"]==i) & (uv_data_filter_1["day"]==j)]["UV_Index"].mean()
            # get max value in ech day
            day_max = uv_data_filter_1[(uv_data_filter_1["month"]==i) & (uv_data_filter_1["day"]==j)]["UV_Index"].max()
            # get month and day according to loop
            uv_temp_df.loc[j-1,"month"] = i
            uv_temp_df.loc[j-1,"day"] = j
            uv_temp_df.loc[j-1,"day_mean"] = day_mean
            uv_temp_df.loc[j-1,"day_max"] = day_max
        # append data into dataframe
        final_data = pd.concat([final_data,uv_temp_df])
    elif i in [4,6,9,11]:
        uv_temp_df = pd.DataFrame(columns=[])
        for j in range(1,30):
            day_mean = uv_data_filter_1[(uv_data_filter_1["month"]==i) & (uv_data_filter_1["day"]==j)]["UV_Index"].mean()
            day_max = uv_data_filter_1[(uv_data_filter_1["month"]==i) & (uv_data_filter_1["day"]==j)]["UV_Index"].max()
            uv_temp_df.loc[j-1,"month"] = i
            uv_temp_df.loc[j-1,"day"] = j
            uv_temp_df.loc[j-1,"day_mean"] = day_mean
            uv_temp_df.loc[j-1,"day_max"] = day_max
        final_data = pd.concat([final_data,uv_temp_df])
    else:
        uv_temp_df = pd.DataFrame(columns=[])
        for j in range(1,28):
            day_mean = uv_data_filter_1[(uv_data_filter_1["month"]==i) & (uv_data_filter_1["day"]==j)]["UV_Index"].mean()
            day_max = uv_data_filter_1[(uv_data_filter_1["month"]==i) & (uv_data_filter_1["day"]==j)]["UV_Index"].max()
            uv_temp_df.loc[j-1,"month"] = i
            uv_temp_df.loc[j-1,"day"] = j
            uv_temp_df.loc[j-1,"day_mean"] = day_mean
            uv_temp_df.loc[j-1,"day_max"] = day_max
        final_data = pd.concat([final_data,uv_temp_df])
final_data = final_data.reset_index()
final_data.drop(columns=["index"])
end_data = pd.DataFrame(columns=[])
# calcuate mean and max for each month and store it in new dataframe
for i in range(1,13):
    month_avg_mean = final_data[(final_data["month"]==i)]["day_mean"].mean()
    month_avg_max = final_data[(final_data["month"]==i)]["day_max"].mean()
    end_data.loc[i-1,"month"] = i
    end_data.loc[i-1,"uv_month_avg_max"] = month_avg_max
    end_data.loc[i-1,"uv_month_avg_mean"] = month_avg_mean
end_data.to_csv("uv_index_monthly.csv")