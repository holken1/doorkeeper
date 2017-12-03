
import requests
import json
from credentials import get_username, get_password
import time

CACHE_REFRESH_MINUTES = 20

loaded_time = 0
weather = {}

forced_rain = False
forced_snow = False
forced_sunny = False
forced_cloudy = False

def force_rain(v):
    global forced_rain
    forced_rain = v

def force_snow(v):
    global forced_snow
    forced_snow = v

def force_sunny(v):
    global forced_sunny
    forced_sunny = v

def force_cloudy(v):
    global forced_cloudy
    forced_cloudy = v

def is_cache_old():
    global loaded_time
    c = int(time.time())
    diff = c - loaded_time
    #print('Age in seconds:', diff)
    return diff > CACHE_REFRESH_MINUTES * 60

def check():
    if is_cache_old():
        load_weather()
        
def load_weather():
    username = get_username()
    password = get_password()
    watsonUrl = 'https://twcservice.eu-gb.mybluemix.net/api/weather/v1/geocode/59.52/17.9/forecast/intraday/3day.json?language=en-US&units=m'
    global weather
    global loaded_time
    print("Laddar väderprognos...")
    r = requests.get(watsonUrl,auth=(username,password))
    weather = json.loads(str(r.text))
    # test that the proper structure was recieved
    _ = weather['forecasts'][0]['precip_type']
    _ = weather['forecasts'][0]['pop']
    _ = weather['forecasts'][1]['precip_type']
    _ = weather['forecasts'][1]['pop']
    loaded_time = int(time.time())
    print("Klart!")

def is_rain():
    if forced_rain:
        return True
    check()
    type1 = weather['forecasts'][0]['precip_type']
    pop1 = weather['forecasts'][0]['pop']
    type2 = weather['forecasts'][1]['precip_type']
    pop2 = weather['forecasts'][1]['pop']
    print(type1, pop1, type2, pop2)
    return (type1 == "rain" or type2 == "rain") and (pop1 > 60 or pop2 > 60)

def is_snow():
    if forced_snow:
        return True
    check()
    type1 = weather['forecasts'][0]['precip_type']
    pop1 = weather['forecasts'][0]['pop']
    type2 = weather['forecasts'][1]['precip_type']
    pop2 = weather['forecasts'][1]['pop']
    print(type1, pop1, type2, pop2)
    return (type1 == "snow" or type2 == "snow") and (pop1 > 60 or pop2 > 60)


def is_cloudy():
    if forced_cloudy:
        return True
    check()
    clds1 = weather['forecasts'][0]['phrase_12char']
    clds2 = weather['forecasts'][1]['phrase_12char']
    print('Clouds: ', clds1, clds2)
    return (clds1 == 'Cloudy' or clds2 == 'Cloudy')


def is_sunny():
    if forced_sunny:
        return True
    check()
    clds1 = weather['forecasts'][0]['phrase_12char']
    clds2 = weather['forecasts'][1]['phrase_12char']
    print('Phrase: ', clds1, clds2)
    return (clds1 == 'Sunny' or clds1 == 'M Sunny' or clds2 == 'Sunny' or clds2 == 'M Sunny')
    
if __name__ == '__main__':
    check()
    print(json.dumps(weather, indent=3))
          
