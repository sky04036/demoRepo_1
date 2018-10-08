# USAGE
# python distance_to_camera.py

# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2




def find_marker(image):
	# convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray,35, 125)

	# find the contours in the edged image and keep the largest one;
	# we'll assume that this is our piece of paper in the image
#找到邊緣圖像中的輪廓並保持最大的輪廓;
#我們假設這是我們在圖片中的一張紙
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    c = max(cnts, key = cv2.contourArea)

	# compute the bounding box of the of the paper region and return it
 #計算紙張區域的邊界框並將其返回
    return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
 #計算並返回製造商到相機的距離
    return (knownWidth * focalLength) / perWidth

# initialize the known distance from the camera to the object, which
# in this case is 24 inches
 #初始化從攝像機到物體的已知距離，在這種情況下
 #為24英寸
KNOWN_DISTANCE = 33.464585

# initialize the known object width, which in this case, the piece of
# paper is 12 inches wide
#初始化已知的物體寬度，在這種情況下，
#紙的寬度為12英寸
KNOWN_WIDTH = 4.4488213

# load the furst image that contains an object that is KNOWN TO BE 2 feet
# from our camera, then find the paper marker in the image, and initialize
# the focal length
#加載包含一個已知為2英尺的對象的第一個圖像
#從我們的相機，然後在圖像中找到紙標記，並初始化
#焦距
image = cv2.imread("00000000007_205.png")
marker = find_marker(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

# loop over the images
#循環圖像
for imagePath in sorted(paths.list_images("images")):
	# load the image, find the marker in the image, then compute the
	# distance to the marker from the camera
 #加載圖像，在圖像中找到標記，然後計算
#從相機到標記的距離
 
    image = cv2.imread(imagePath)
    marker = find_marker(image)
    inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])

	# draw a bounding box around the image and display it
 #＃在圖像周圍繪製一個邊界框並顯示它
    box = cv2.cv.BoxPoints(marker) if (imutils.is_cv2()) else cv2.boxPoints(marker)
    box = np.int0(box)
    cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
    cv2.putText(image, "%.2fm" % ((inches / 4.4488213)*30.48/100),
                (image.shape[1], image.shape[0]), cv2.FONT_HERSHEY_SIMPLEX,
                2.0, (0, 255, 0), 3)
    cv2.namedWindow("enhanced", cv2.WINDOW_NORMAL);
    cv2.resizeWindow("enhanced", 600, 800);
    cv2.imshow("enhanced",image)
    cv2.waitKey(0)
    #('z') or  closekey_1 == ord('Z'):
        #break
    