import cv2
import os

# picks up all png files in the folder you are in
# and superimposes it on a blank image so that you get
# a nice white boundary around the whole image

# You would need OpenCV of course

l_img = cv2.imread("/home/nikhil/bound.jpg")


for filename in os.listdir("."):
	if ".png" in filename:
		s_img = cv2.imread(filename)
		x_offset = y_offset = 5
		print "working on "+filename
		l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
		cv2.imwrite("/home/nikhil/temp/"+filename, l_img)
