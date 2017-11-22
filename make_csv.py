#
#			CONVERT TO CSV
#


import nltk
import os
# This code is for picking up files from two directories: pos and neg
# containing positive and negative content each file in pos/neg containing 
# written content which is positive/negative review of a movie.
# This code picks up each review and inserts it into a csv file with the first
# column containing the review and the next column contaning the sentiment
# denoted as 1:positive and 0:negative



import csv


		# FOR POSITIVE FILES


positive_path = "data/pos/"
global_list_positive = []

for filename in os.listdir(positive_path):
	pos_file = open(positive_path + filename, 'r')
	l = []
	l.append(1)
	l.append(pos_file.read())
	global_list_positive.append(l)

with open("output.csv", "wb") as csv_writer:
	writer = csv.writer(csv_writer)
	writer.writerows(global_list_positive)




		#FOR NEGATIVE FILES

negative_path = "data/neg/"
global_list_negative = []

for filename in os.listdir(negative_path):
	neg_file = open(negative_path + filename, 'r')
	l = []
	l.append(-1)
	l.append(neg_file.read())
	global_list_negative.append(l)

with open("output.csv", 'a') as csv_writer:
	writer = csv.writer(csv_writer)
	writer.writerows(global_list_negative)