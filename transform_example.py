from transform import four_points_transform
import numpy as np
import argparse
import cv2

# contruct the argument parse and parse the arguements
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-c", "--coords",
    help = " comma seperated list of points" )
args = vars(ap.parse_args())

# Load the image and grab the source corrdinates (i.e the list of (x, y) points)

image = cv2.imread(args["image"])
pts = np.array(eval(args["coords"]) , dtype = "float32")

# apply the four points transofrm to obtain a "birds eye view'"

warped = four_points_transform(image,pts)

#show the original warped image
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)
