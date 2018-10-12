#!/usr/bin/env python3

#import LCD_1in44
#import LCD_Config

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

try:
	def main():
		#LCD = LCD_1in44.LCD()
		
		#print "**********Init LCD**********"
		#Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
		#LCD.LCD_Init(Lcd_ScanDir)
		
		#LCD.LCD_ShowImage(image,0,0)
		#LCD_Config.Driver_Delay_ms(500)

		print("********** Start GIF of single  image **********")
		
		cat = imageio.mimread("cats/Resized/cat_1.gif")
		numOfFrames = len(cat)
		print("Total {} frames in the gif!".format(numOfFrames))

		# convert form RGB to BGR 
		# imgs = cat
		imgs = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in cat]

		# show the single images
		i = 0
		while True:
			LCD_ShowImageAsArray(imgs[i], 0, 0)
			cv2.imshow("gif", imgs[i])
			if cv2.waitKey(100)&0xFF == 27:
				break
			i = (i+1)%numOfFrames

		cv2.destroyAllWindows()

		time.sleep()
		
	if __name__ == '__main__':
		main()

except Exception as er:
	print("Catched exception! Error: " + str(er))