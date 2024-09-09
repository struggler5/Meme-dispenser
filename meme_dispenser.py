import random as rn
import os
import cv2 as cv

# using black magic to insert all the jpg files in the imgs list in 1 line
imgs = [file for file in os.listdir() if file.endswith('.jpg')]

def img_meme():
    img1 = rn.choice(imgs)
    img2 = rn.choice(imgs)
    img3 = rn.choice(imgs)
    scale_factor = 0.3
    # img 1
    cvIMG1 = cv.imread(img1)
    cvIMG1 = cv.resize(cvIMG1, (400,600), fx=scale_factor, fy=scale_factor, interpolation=cv.INTER_AREA)
    #cvIMG1 = cv.resize(cvIMG1, (400,600))
    cv.imshow("meme1",cvIMG1)
    cv.moveWindow('meme1',0,50)

    # img 2

    cvIMG2 = cv.imread(img2)
    cvIMG2 = cv.resize(cvIMG2, (400,600), fx=scale_factor, fy=scale_factor, interpolation=cv.INTER_AREA)
    #cvIMG2 = cv.resize(cvIMG2, (400,600))
    cv.imshow("meme2",cvIMG2)
    cv.moveWindow('meme2',575,50)

    # img 3

    cvIMG3 = cv.imread(img3)
    cvIMG3 = cv.resize(cvIMG3, (400,600), fx=scale_factor, fy=scale_factor, interpolation=cv.INTER_AREA)
    #cvIMG3 = cv.resize(cvIMG3, (400,600))
    cv.imshow("meme3",cvIMG3)
    cv.moveWindow('meme3',1150,50)


    cv.waitKey(0)
    cv.destroyAllWindows()

img_meme()

