import cv2
import progressbar
import pickle

positions = pickle.load(open("positionsGoodnew2.p", "rb"))

max_x = max(positions, key=lambda item:item[0])[0]
max_y = max(positions, key=lambda item:item[1])[1]

min_x = min(positions, key=lambda item:item[0])[0]
min_y = min(positions, key=lambda item:item[1])[1]

print(max_x, max_y, min_x, min_y)

vid = cv2.VideoCapture("colors.mp4")

positions = [(x - min_x, y - min_y) for x, y in positions]
allPixels = []


# num_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT)) - 2
num_frames = 2000


with open("allPixels.txt", "w") as file:

    for i in progressbar.progressbar(range(num_frames)):

        _, img = vid.read()
        
        img = cv2.resize(img, (max_x - min_x + 1, max_y - min_y + 1))

        for position in positions:
            if position[0] == 1079 - min_x and position[1] == 810 - min_y:
                file.write("0,0,0|")
            else:
                file.write(str(img[position[1]][position[0]][0]) + "," + str(img[position[1]][position[0]][1]) + "," + str(img[position[1]][position[0]][2]) + "|")

        file.write("\n")

