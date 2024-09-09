# The meme dispenser

*The initial directory had 907 files but github has a limit for files so I only uploaded 72 memes :(*
## Use
> You could just drag and drop the `meme_dispenser.py` file in your personal meme directory
*Warning:for now it only works with .jpg files, and sadly no video*
## Dependecies
- python 3.7 and above
- cv2
- os


## How it works?
1. it looks for all the jpg files and puts them in a list
```py
imgs = [file for file in os.listdir() if file.endswith('.jpg')]
```

2. Then it selects a random file
with :
```py
    img1 = rn.choice(imgs)
```
*I abreviated random as rn for convenience*

3. Then the image is read by cv2 and resized then placed

```py
    cvIMG1 = cv.imread(img1)
    cvIMG1 = cv.resize(cvIMG1, (400,600), fx=scale_factor, fy=scale_factor, interpolation=cv.INTER_AREA)
    #cvIMG1 = cv.resize(cvIMG1, (400,600))
    cv.imshow("meme1",cvIMG1)
    cv.moveWindow('meme1',0,50)
```

*You can quit by pressing 'd', and I abreviated 'cv2' as 'cv' for conveniece*
## Placement and size

> the code was originally made for my monitor witch is a 1200x600 so the placement might seem weird on other resolutions

*you can modify here:*
```py
cv.moveWindow('meme1',0,50)
```

 The code will display 3 memes equally separated (if u are on a 1200x600), sadly I bruteforced it but I might change it later so it can be easily change with one variable

