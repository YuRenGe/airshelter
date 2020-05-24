import urllib3, sys
import certifi
# get three active fire data from website
method = 'GET'
MODIS_url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Australia_NewZealand_24h.csv"
SNPP_url="https://firms.modaps.eosdis.nasa.gov/data/active_fire/suomi-npp-viirs-c2/csv/SUOMI_VIIRS_C2_Australia_NewZealand_24h.csv"
NOAA_url="https://firms.modaps.eosdis.nasa.gov/data/active_fire/noaa-20-viirs-c2/csv/J1_VIIRS_C2_Australia_NewZealand_24h.csv"
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
MODIS_request = http.request(method, MODIS_url)
# restore data
with open('C:\\Python\\airshelter\\get_data\\MODIS_C6_Australia_NewZealand_24h.csv', 'wb') as f:
    f.write(MODIS_request.data)
    f.close()
SNPP_request = http.request(method, SNPP_url)
with open('C:\\Python\\airshelter\\get_data\\SUOMI_VIIRS_C2_Australia_NewZealand_24h.csv', 'wb') as f:
    f.write(SNPP_request.data)
    f.close()
NOAA_request = http.request(method, NOAA_url)
with open('C:\\Python\\airshelter\\get_data\\J1_VIIRS_C2_Australia_NewZealand_24h.csv', 'wb') as f:
    f.write(NOAA_request.data)
    f.close()
sys.exit()