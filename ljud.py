import simpleaudio as sa
rain_obj = sa.WaveObject.from_wave_file("/home/pi/kod/ljud/regn.wav")
snow_obj = sa.WaveObject.from_wave_file("/home/pi/kod/ljud/snö.wav")
sun_obj = sa.WaveObject.from_wave_file("/home/pi/kod/ljud/soligt.wav")
mulet_obj = sa.WaveObject.from_wave_file("/home/pi/kod/ljud/mulet.wav")
lock_obj = sa.WaveObject.from_wave_file("/home/pi/kod/ljud/bra-dag.wav")

def play(obj):
    play_obj = obj.play()
    play_obj.wait_done()

def play_rain():
    play(rain_obj)
    
def play_snow():
    play(snow_obj)

def play_sunny():
    play(sun_obj)

def play_good_day():
    play(lock_obj)

def play_cloudy():
    play(mulet_obj)
