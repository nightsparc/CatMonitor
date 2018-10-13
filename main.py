#!/usr/bin/env python3

# Import LCD drivers
import LCD_1in44
import LCD_Config

# Import time and system stuff
import time
import os
import random

# Import imageio stuff
import imageio

LCD = LCD_1in44.LCD()

def displayGIF(GIFImage, name):
    numOfFrames = len(GIFImage)
    print("Total {} frames in the gif \"{}\"!".format(numOfFrames, name))

    # show the single images
    try:
        repeats = 1
        if numOfFrames <= 10:
            repeats = 3
        elif numOfFrames <= 25:
            repeats = 2
        i = 0
        for x in range(0, repeats * numOfFrames):
            LCD.LCD_ShowImageAsArray(GIFImage[i],0,0)
            time.sleep(0.06)
            i = (i+1)%numOfFrames
        else:
            print("End of OpenCV vis loop :)")
    except Exception as er:
        print("OpenCV vis exception! Error: " + str(er))

try:
    def main():        
        print("**********Init LCD**********")
        Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
        LCD.LCD_Init(Lcd_ScanDir)
        LCD_Config.Driver_Delay_ms(500)

        # print("********** Start GIF of single  image **********")
        # cat = imageio.mimread("cats/cat_1.gif")
        # numOfFrames = len(cat)
        # print("Total {} frames in the gif!".format(numOfFrames))
        
        # # show the single images
        # i = 0

        # while True:
        #     LCD.LCD_ShowImageAsArray(cat[i],0,0)
        #     time.sleep(0.05)
        #     i = (i+1)%numOfFrames

        # Begin with random selected GIF
        print("********** Start VIS of random gif ****************")
        directory = "cats/Resized"

        while True:
            #filename = random.choice(os.listdir("cats/Resized"))
            # last part ensures that opened file is indeed a file
            filename = random.choice([x for x in os.listdir(directory) if os.path.isfile(os.path.join(directory, x))]) 
            print("Random choice file: " + directory + "/" + filename)
            try:
                catRandom = imageio.mimread(directory + "/" + filename)
                displayGIF(catRandom, "random cat " + filename)
            except Exception as er:
                print("ImageIO mimread error: " + str(er))
        
        print("Stopping cat test monitor. Goodbye :)")
        
    if __name__ == '__main__':
        main()
except Exception as er:
        print("Catched exception! Error: " + str(er))
