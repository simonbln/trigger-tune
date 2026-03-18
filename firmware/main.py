from machine import Pin, UART, lightsleep
import neopixel
import time
import random
from dfplayermini import DFPlayerMini


print("start")


input_signal = Pin(2, Pin.IN, Pin.PULL_UP) 
pixel = neopixel.NeoPixel(Pin(16), 1)
pixel2 = neopixel.NeoPixel(Pin(28), 1)

class Colors:
    RED     = (50, 0, 0)
    GREEN   = (0, 50, 0)
    BLUE    = (0, 0, 50)
    YELLOW  = (50, 50, 0)
    CYAN    = (0, 50, 50)
    MAGENTA = (50, 0, 50)
    WHITE   = (50, 50, 50)
    OFF     = (0, 0, 0)

def set_pixel_color(color_rgb):
    pixel[0] = color_rgb
    pixel2[0]= color_rgb
    pixel.write()
    pixel2.write()
    
set_pixel_color(Colors.WHITE)

time.sleep(1)
player = DFPlayerMini(1,4,5)
time.sleep(1)
while True:
    print ("Reset")
    if player.reset() == True:
        print ("Reset: OK")
        break
    time.sleep(1)

time.sleep(1)
player.select_source('sdcard')

print ("Read Num files")
count_songs = player.query_num_files()
print (f"Num files {count_songs}")

print ("Read volume")
read_value = player.get_volume()
print (f"Volume {read_value}")

player.set_volume(30)

print ("Read volume")
read_value = player.get_volume()
print (f"Volume {read_value}")

ready_for_detection = True

last_song = 0

def play_random():
    global last_song
    if count_songs > 0:
        if count_songs == 1:
            # If only one song exists, just play it
            random_song = 1
        else:
            # Pick a song, but not the same as the last one
            random_song = last_song
            while random_song == last_song:
                random_song = random.randint(1, count_songs)
        
        # Update last_song for next time
        last_song = random_song
        
        print(f"Action: Playing random track {random_song}")
        player.play(random_song)
        #player.play(1)
    else:
        print("Error: No songs found on SD card.")
        set_pixel_color(Colors.RED)

play_start_time = 0
is_playing = False

while True:
    current_time = time.ticks_ms()

    if is_playing and time.ticks_diff(current_time, play_start_time) > 10000:
        player.stop()
        is_playing = False
        print("Time up: Stopped playing")
        
    if count_songs == 0:
        set_pixel_color(Colors.RED)
        time.sleep(2)
    elif input_signal.value() == 0:
        if ready_for_detection:
            ready_for_detection = False
            set_pixel_color(Colors.BLUE)
            play_random()
            play_start_time = time.ticks_ms()
            is_playing = True            
            time.sleep(1)
        else:
            set_pixel_color(Colors.YELLOW)
            time.sleep(0.5)
    else:
        ready_for_detection = True
        set_pixel_color(Colors.GREEN)
    time.sleep(0.05)