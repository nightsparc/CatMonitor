#!/usr/bin/env python

# Import LCD drivers
import LCD_1in44
import LCD_Config

# Import GIL libs
#import Image
#import ImageDraw
#import ImageFont
#import ImageColor

# Import time stuff
import time

# Import imageio stuff
import imageio

try:
    def main():
        LCD = LCD_1in44.LCD()
        
        print("**********Init LCD**********")
        Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
        LCD.LCD_Init(Lcd_ScanDir)
        LCD_Config.Driver_Delay_ms(500)

        print("********** Start GIF of single  image **********")
        cat = imageio.mimread("cats/cat_1.gif")
        numOfFrames = len(cat)
        print("Total {} frames in the gif!".format(numOfFrames))
        
        #LCD.LCD_ShowImage(image,0,0)

        # show the single images
        i = 0

        while True:
            LCD.LCD_ShowImageAsArray(cat[i],0,0)
            time.sleep(0.05)
            i = (i+1)%numOfFrames
        
    if __name__ == '__main__':
        main()
except Exception as er:
        print("Catched exception! Error: " + str(er))
