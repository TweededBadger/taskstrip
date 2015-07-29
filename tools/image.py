from neopixel import *

from PIL import Image

def convert_to_colors(src):
    im = Image.open(src) #Can be many different formats.
    pix = im.load()
    colors = []


    for y in range(im.size[1]):
        for x in range(im.size[1]):
            print pix[x,y]
            color = Color(pix[x,y][0], pix[x,y][1], pix[x,y][2])
            colors.append(color)
    print im.size

    return colors

