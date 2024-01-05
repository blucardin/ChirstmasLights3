
import pickle
import cv2
import board
import neopixel
import time
import progressbar

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 500


ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

while True:
    with open("allPixels.txt", "r") as file:

        num_frames = 2000

        for idx in range(0, num_frames):
            pixels.fill((0, 0, 0))
            file.readline()
            line = file.readline().split("|")
            line.pop()
            for i, color in enumerate(line):
                r, g, b = color.split(",") # R G B
                d = 2
                pixels[i] = (int(g)//d, int(b)//d, int(r)//d)
            pixels.show()
 

