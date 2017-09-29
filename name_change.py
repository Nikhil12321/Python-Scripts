# edit names of all files in a folder

import os
for filename in os.listdir("."):
	os.rename(filename, "wisdom_"+filename)
