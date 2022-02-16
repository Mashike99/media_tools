######################
#movie_frame_splitter#
######################

import pims
import imageio
import numpy as np
import os

def movie_splitter(filename, target_dir):
	"""
	Take a movie file supported by PIMS.ImageIOReader
	Split into individual frames
	Return a directory of greyscale images
	"""
	import pims
	import imageio
	import numpy as np
	import os

	assert os.path.exists(filename), "This file does not exist"
	try:
		assert os.path.exists(target_dir)
	except AssertionError:
		print(f"Making directory '{target_dir}' for image output")
		os.mkdir(target_dir)

	vid = pims.ImageIOReader(filename)
	t = vid.frame_rate
	vlen = len(vid)-1

	target_dir += "/"
	print(target_dir)

	for fr_i in range(vlen):
		frame = vid[fr_i][:,:,0]
		imageio.imwrite(f"{target_dir}{fr_i}.jpeg", frame)

	print(f"Video {filename} frames captured!")

import glob

vid_list = glob.glob('*.mp4')
dir_list = []
for vid_name in vid_list:
	name = vid_name.split('_overlay')[0] + "_images"
	dir_list.append(name)

print(dir_list)
print(vid_list)

for i in range(len(vid_list)):
	movie_splitter(vid_list[i], dir_list[i])

print("Completed!")

movie_splitter(filename = "47_02_overlay.mp4", target_dir = "47_02_images_2")