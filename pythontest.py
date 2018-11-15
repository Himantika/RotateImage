# To rotate any bitmap, place the file in the pythontest.py folder and name it sample.
# The output will be a bitmap called clockwise.bmp in the same folder.
# RotateImage() rotates an image 90 degrees clockwise only if the height and width of image is same

from PIL import Image

img = Image.open('sample.bmp')

def RotateImage(img):
    width, height = img.size
    if width == height:
        image_clockwise = img.rotate(270)
        image_clockwise.save('clockwise.bmp')
        print "You have rotated you image clockwise. Please check!"
    else:
        print "Sorry, select the image with same dimensions"

RotateImage(img)