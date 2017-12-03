import simpleaudio as sa
rain_obj = sa.WaveObject.from_wave_file("/home/pi/kod/test/regn.wav")

def play_rain():
    play_obj = rain_obj.play()
    play_obj.wait_done()



