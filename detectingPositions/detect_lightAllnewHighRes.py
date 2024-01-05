import cv2
import numpy as np
import board
import neopixel
import time
import pickle
import progressbar

vid = cv2.VideoCapture(-1)

vid.set(cv2.CAP_PROP_AUTOFOCUS, 0)

vid.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)

time.sleep(1)

def genPositions(radius):

    pixel_pin = board.D18

    num_pixels = 500

    ORDER = neopixel.GRB

    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
    )

    positions = []
    GaussianRadius = radius

    pixels.fill((0, 0, 0))
    pixels.show()


    # cv2.namedWindow('image')
    # cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
    
    for i in progressbar.progressbar(range(0, num_pixels)):

        pixels.fill((0, 0, 0))

        pixels[i] = (30, 30, 30)
        pixels.show()
        
        ret, frame = vid.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        blur = gray
        if GaussianRadius > 0:
            blur = cv2.GaussianBlur(gray, (GaussianRadius, GaussianRadius), 0)

        (_, _, _, maxLoc) = cv2.minMaxLoc(blur)

        # cv2.circle(frame, maxLoc, GaussianRadius, (255, 0, 0), 2)

        # cv2.imshow('image',frame)

        positions.append(maxLoc)
        
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break

    
    pixels.fill((20, 20, 20))
    pixels.show()

    positions.pop(0)

    return positions

if __name__ == "__main__":
    positions = genPositions(15)

    pickle.dump(positions, open("positionsGoodnew2.p", "wb"))
    time.sleep(3)

    ret2, frame2 = vid.read()
    ret2, frame2 = vid.read()

    cv2.imwrite('positions/positions12_.png', frame2)

    for x in range(0, len(positions)):
        color = (0, 0, 255)
        if x % 2 == 0:
            color = (255, 0, 0)
        cv2.circle(frame2, positions[x], 5, color, 2)

    cv2.imwrite('positions/positions12.png', frame2)


