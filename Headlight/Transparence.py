import math
import sys
import numpy as np
import cv2
from PIL import Image, ImageEnhance
import os
import cv2 as cv
import numpy as np



image_dir = "C:/Users/Amiran/Desktop/Second-ISI/headlights/Feature Extraction/main-headlight/Output/Contour"
output_dir = "C:/Users/Amiran/Desktop/Second-ISI/headlights/Feature Extraction/main-headlight/Output/Transparent"

def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)






for _, _, image_names in os.walk(image_dir):
		for image_name in image_names:
			if '.jpg' in image_name:
				filepath = os.path.join(image_dir, image_name)
				dstpath = os.path.join(output_dir, image_name)
				#dstpath2 = os.path.join(output_dir2, image_name)
				img = Image.open(filepath)
				rgba = img.convert("RGBA")
				datas = rgba.getdata()
				newData = []
				for item in datas:
					if item[0] < 100 and item[1] < 100 and item[2] < 100:  # finding black colour
						# replacing it with a transparent value
						newData.append((255, 255, 255, 0))
					else:
						newData.append(item)

				rgba.putdata(newData)
				rgba.save(dstpath, "PNG")


first_image_dir = "C:/Users/Amiran/Desktop/Second-ISI/headlights/Feature Extraction/main-headlight/Images"
second_image_dir = "C:/Users/Amiran/Desktop/Second-ISI/headlights/Feature Extraction/main-headlight/Output/Transparent"
output_dir2 = "C:/Users/Amiran/Desktop/Second-ISI/headlights/Feature Extraction/main-headlight/Output/Final"


def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)

for _, _, image_names_1 in os.walk(first_image_dir):
		for image_name_1 in image_names_1:
			if '.jpg' in image_name_1:
				filepath_first_image = os.path.join(first_image_dir, image_name_1)
				dstpath = os.path.join(output_dir, image_name_1)
				dstpath2 = os.path.join(output_dir2, image_name_1)
				#images = []
				img = (filepath_first_image)
				#images.append(img)
				for _, _, image_names_2 in os.walk(second_image_dir):
					for image_name_2 in image_names_2:
						if '.jpg' in image_name_2:
							if image_name_1 == image_name_2:

							    filepath_second_image = os.path.join(second_image_dir, image_name_2)
							    dstpath = os.path.join(output_dir, image_name_2)
							    dstpath2 = os.path.join(output_dir2, image_name_2)
							    dstpath2png = dstpath2.split(".") [0]
							    img_2 = (filepath_second_image)
							    watermark_with_transparency(img, dstpath2png + '.png',
							     img_2, position=(0,0))

