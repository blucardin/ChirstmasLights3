
import pickle
import cv2
import board
import neopixel
import time
import progressbar

vid = cv2.VideoCapture(-1)

#lock autofocus
vid.set(cv2.CAP_PROP_AUTOFOCUS, 0)

# # neew code
# vid.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
# vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)


pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 500


ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('outputColours5.mp4', fourcc, 30.0, (640,  480))

with open("allPixels.txt", "r") as file:

    # num_frames = 1000
    num_frames = 449
    

    for idx in progressbar.progressbar(range(num_frames)):
        log = time.time()
        pixels.fill((0, 0, 0))
        line = file.readline().split("|")
        line.pop()
        for i, color in enumerate(line):
            r, g, b = color.split(",") # R G B
            d = 2
            pixels[i] = (int(g)//d, int(b)//d, int(r)//d)
        pixels.show()


        ret, frame = vid.read()
        out.write(frame)

    # pad the filename with leading zeros

# Release everything if job is finished
print("Processing complete")
vid.release()
out.release()
cv2.destroyAllWindows()
 

