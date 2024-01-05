import cv2
import progressbar
import pickle

positions = pickle.load(open("positionsGoodnew.p", "rb"))

max_x = max(positions, key=lambda item:item[0])[0]
max_y = max(positions, key=lambda item:item[1])[1]

min_x = min(positions, key=lambda item:item[0])[0]
min_y = min(positions, key=lambda item:item[1])[1]

img = cv2.imread('Image.png')

positions = [(x - min_x, y - min_y) for x, y in positions]
allPixels = []

num_frames = 1

with open("allPixels.txt", "w") as file:
    img = cv2.resize(img, (max_x - min_x + 1, max_y - min_y + 1))

    for position in positions:
        file.write(str(img[position[1]][position[0]][0]) + "," + str(img[position[1]][position[0]][1]) + "," + str(img[position[1]][position[0]][2]) + "|")

    file.write("\n")

