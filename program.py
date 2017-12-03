## huvudprogram

from ljud import *
from weather import *
from hw import *
from time import sleep

# hämta vädret nu!
load_weather()
set_green(True)

force_rain(True)

while True:
    if is_motion() and is_rain ():
        set_red(True)
        set_green(False)
        play_rain()
        sleep(10)
        set_green(True)
        set_red(False)
    sleep(1)       
