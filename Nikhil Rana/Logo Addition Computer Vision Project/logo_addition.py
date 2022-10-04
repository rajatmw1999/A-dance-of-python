import cv2
import argparse 
import numpy as np
import imutils 
import os
import time
from argparse import ArgumentParser


# ap = ArgumentParser()

# ap.add_argument('-i', '--image', required=True, type=str, \
# 				help="Image which add to the background")
# ap.add_argument('-v', '--video', required=True, type=str, \
# 				help="video to which has to add background")
# ap.add_argument('-o', '--output', required=True, type=str, \
# 				help="output directory for output video")

# args = vars(ap.parse_args())


imagePath = os.path.join(os.getcwd(), "np_logo.png")
videoPath = os.path.join(os.getcwd(), "dance.mp4")


logo = cv2.imread(imagePath)

logo = imutils.resize(logo, width=380)

cap = cv2.VideoCapture(videoPath)
time.sleep(2.0)

writer = None

height, width, channel = logo.shape

print(f'Logo Image shape: {logo.shape}')
# print(f'frame shape: {frame.shape}')

# 6, 10, 68
# 30, 36, 122

lower_val = np.array([6, 10, 68])
upper_val = np.array([30, 36, 122])

print("[INFO] Logo Addition starts...")

while True:

	is_frame, frame = cap.read()
	# print(f"Frame Shape: {frame.shape}")

	# if(!is_frame):
	# 	break

	if not is_frame:
		break

	# Capturing the dimension on the wall where we want to
	# place that logo.

	mini_frame = frame[400:400+height, 875:875+width, :]

	# Converting the HSV image.
	
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Creating the binary mask

	mask = cv2.inRange(hsv_frame, lower_val, upper_val)

	# dilating the mask.

	dilation = cv2.dilate(mask, np.ones((3,3), np.uint8), 7)

	mini_dil = np.zeros_like(mini_frame)

	mini_dil[:, :, 0] = dilation[400:400+height, 875:875+width]
	mini_dil[:, :, 1] = dilation[400:400+height, 875:875+width]
	mini_dil[:, :, 2] = dilation[400:400+height, 875:875+width]

	# print(f'Shape of Mini-dil: {mini_dil.shape}')

	logo_copy = logo.copy()

	# setting the pixel values to 0 where pixel values of mask is Black or 0. 
	logo_copy[mini_dil==0] = 0

	# setting the pixel values to 0 where pixel values of logo is Black or 0.
	logo_copy[logo==0] = 0

	mini_frame[logo_copy != 0] = 0

	# merging the images
	merge_frame = mini_frame + logo_copy

	frame[400:400+height, 875:875+width, :] = merge_frame

	# show_frame = cv2.resize(frame, (480,270), interpolation=cv2.INTER_AREA)

	# cv2.imshow("Mask", mask)
	# cv2.imshow("HSV Frame", hsv_frame)
	# cv2.imshow("Mini Dilation", mini_dil)
	# cv2.imshow("Logo Copy", logo_copy)
	# cv2.imshow("Merge Frame", merge_frame)
	# cv2.imshow("Output Frame", show_frame)

	if writer==None:
		fourcc = cv2.VideoWriter_fourcc(*'MJPG')
		writer = cv2.VideoWriter("logo_addition_approach.avi", fourcc, 25, \
				 (frame.shape[1], frame.shape[0]), True)

	if writer is not None:
		writer.write(frame)

	# if cv2.waitKey(0) & 0xFF == ord('q'):
	# 	break

print("Done...")
cap.release()
cv2.destroyAllWindows()
writer.release()


'''
Multiplication Way. As in blog post.
setting the pixel values to 1 where pixel values of mask is Black or 0. 
	logo_copy[mini_dil==0] = 1

setting the pixel values to 0 where pixel values of logo is Black or 0.
	logo_copy[logo==0] = 1

	mini_frame[logo_copy != 1] = 1

merging the images
	merge_frame = mini_frame * logo_copy
'''




# CBVIKA2K