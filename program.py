## huvudprogram

from ljud import *
from weather import *
from hw import *
from time import sleep

# hämta vädret nu!
load_weather()
set_green(True)

#force_rain(True)

while True:
    if is_motion():
        set_red(True)
        set_green(False)
        if is_snow():
            play_snow()
        else:
            if is_rain():
                play_rain()
            else:
                if is_cloudy():
                    play_cloudy()
                else:
                    if is_sunny():
                        play_sunny()
        play_good_day()
        sleep(5)
        set_green(True)
        set_red(False)
    sleep(1)       
