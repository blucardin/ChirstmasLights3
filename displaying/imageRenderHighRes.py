#get the positions list from the piclke file
import pickle
import cv2
import board
import neopixel

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 500


ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)


positions = pickle.load(open("positionsGoodnew.p", "rb"))

# find the max value x and y coordinates
max_x = max(positions, key=lambda item:item[0])[0]
max_y = max(positions, key=lambda item:item[1])[1]

# find the min value x and y coordinates
min_x = min(positions, key=lambda item:item[0])[0]
min_y = min(positions, key=lambda item:item[1])[1]

# load img.png
filename = 'testCard_1.png'
img = cv2.imread('/home/nvirjee/code/testImages/' + filename)

# resize the image to fit the screen
img = cv2.resize(img, (max_x - min_x + 1, max_y - min_y + 1))

# shift the positions to be relative to the new image
positions = [(x - min_x, y - min_y) for x, y in positions]

d = 2
# loop through the positions and turn the pixels on if they are white
for idx, position in enumerate(positions):
    pixels[idx] = (img[position[1], position[0]][1]//d, img[position[1], position[0]][2]//d, img[position[1], position[0]][0]//d)

pixels.show()


# take a picture of the screen
vid = cv2.VideoCapture(-1)

#lock autofocus
vid.set(cv2.CAP_PROP_AUTOFOCUS, 0)

# neew code
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)

ret, frame = vid.read()

# save the image
cv2.imwrite('imagesProduced/new3/' + filename, frame)
print('imagesProduced/new3/' + filename)

ret, frame = vid.read()

# print the width and height of frame[min_y:max_y+1, min_x:max_x+1]
# print the width and height of img

print(frame[min_y:max_y+1, min_x:max_x+1].shape)
print(img.shape)

cv2.imwrite('imagesProduced/new3/' + filename, frame)

# overlay the image on the frame at the correct position, but make it transparent
frame[min_y:max_y+1, min_x:max_x+1] = cv2.addWeighted(frame[min_y:max_y+1, min_x:max_x+1], 0.7, img, 0.3, 0)

# for each position circle it on frame
for position in positions:
    x, y = position
    cv2.circle(frame, (x + min_x, y + min_y), 2, (0, 0, 255), -1)

# show the image
cv2.imwrite('imagesProduced/new3/' + "overlay" + filename, frame)
print('imagesProduced/new3/' + "overlay" + filename)

