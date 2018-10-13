#!/usr/bin/env python3

import os
import random
import imageio
import time
import numpy as np

# For visualization and stuff
import cv2

def LCD_ShowImageAsArray(Image,Xstart,Ystart):
	if (Image.all() == None):
		return
	imwidth = Image.shape[0] # width
	imheight = Image.shape[1] # height
	if imwidth != 128 or imheight != 128:
		raise ValueError('Image must be same dimensions as display \
			({0}x{1}).' .format(128, 128))
	pix = np.zeros((128,128,2), dtype = np.uint8)
	pix[...,[0]] = np.add(np.bitwise_and(Image[...,[0]],0xF8),np.right_shift(Image[...,[1]],5))
	pix[...,[1]] = np.add(np.bitwise_and(np.left_shift(Image[...,[1]],3),0xE0),np.right_shift(Image[...,[2]],3))
	pix = pix.flatten().tolist()

def displayGIFWithOpenCV(GIFImage, name):
	numOfFrames = len(GIFImage)
	print("Total {} frames in the gif \"{}\"!".format(numOfFrames, name))
	# convert form RGB to BGR 
	imgs = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in GIFImage]

	# show the single images
	i = 0
	try:
		repeats = 1
		if numOfFrames <= 10:
			repeats = 3
		elif numOfFrames <= 25:
			repeats = 2
		for x in range(0, repeats * numOfFrames):
			LCD_ShowImageAsArray(imgs[i], 0, 0)
			cv2.namedWindow("cat")
			cv2.imshow("cat", imgs[i])
			if cv2.waitKey(60)&0xFF == 27:
				break
			i = (i+1)%numOfFrames
		else:
			print("End of OpenCV vis loop :)")
	except Exception as er:
		print("OpenCV vis exception! Error: " + str(er))

try:
	def main():
		#LCD = LCD_1in44.LCD()
		
		#print "**********Init LCD**********"
		#Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
		#LCD.LCD_Init(Lcd_ScanDir)
		
		#LCD.LCD_ShowImage(image,0,0)
		#LCD_Config.Driver_Delay_ms(500)

		# print("********** Start GIF of single  image **********")
		# cat = imageio.mimread("cats/Resized/cat_1.gif")
		# displayGIFWithOpenCV(cat, "cat")

		# Begin with random selected GIF
		print("********** Start VIS of random gif ****************")
		dir_path = os.path.dirname(os.path.realpath(__file__))
		directory = dir_path + "/cats/Resized"
		print("Directory: " + directory)

		for x in range(1, 20):
			#filename = random.choice(os.listdir("cats/Resized"))
			filename = random.choice([x for x in os.listdir(directory) if os.path.isfile(os.path.join(directory, x))]) # last part ensures that opened file is a file
			print("Random choice file: " + directory + "/" + filename)
			try:
				catRandom = imageio.mimread(directory + "/" + filename)
				displayGIFWithOpenCV(catRandom, "random cat " + filename)
			except Exception as er:
				print("ImageIO mimread error: " + str(er))
		
		# Destroy all created windows at end
		cv2.destroyAllWindows()

		print("Stopping cat test monitor. Goodbye :)")
		
	if __name__ == '__main__':
		main()

except Exception as er:
	print("Catched exception! Error: " + str(er))
