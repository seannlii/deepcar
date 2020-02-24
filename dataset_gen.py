import os
import shutil
import random
from PIL import Image

distro_percent = {"train":0.8,"dev":0.1,"test":0.1}
distro = {}
base_dir = "/mnt/f/VMMRdb/"
classList = os.listdir(base_dir)

im_dims = {}
im_dims["w"] = 0
im_dims["h"] = 0
ii = 0

for folder in ["train","dev","test"]:
	if not os.path.exists(base_dir + folder):
		os.mkdir(base_dir + folder)

for i, className in enumerate(classList):
	exampleList = os.listdir(base_dir + className)
	example_count = len(exampleList)
	print("class " + className + " has count: " , len(exampleList))
	for folder in ["train","dev","test"]:
		if not os.path.exists(base_dir + folder + "/" + className):
			os.mkdir(base_dir + folder + "/" + className)
		distro[folder] = round(example_count * distro_percent[folder])
		for count in range(distro[folder]):
			ran = random.randint(0,len(exampleList) - 1)
			fileName = exampleList[ran]
			shutil.move(base_dir + className + "/" + fileName, base_dir + folder + "/" + className + "/" + fileName)
			exampleList.remove(fileName)
            
			#gathering image data
			im = Image.open(base_dir + folder + "/" + className + "/" + fileName)
			
			w,h = im.size
			im_dims["w"] += w
			im_dims["h"] += h
			ii += 1
			if len(exampleList) == 0: 
				break
		exampleCount = os.listdir(base_dir + folder + "/" + className)
		print(folder + ":", len(exampleCount))
print("Avg W is ",im_dims["w"]/ii)
print("Avg h is ",im_dims["h"]/ii)

