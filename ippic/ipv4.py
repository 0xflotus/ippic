import netaddr, sys, os
from PIL import Image
from .util import *


def _ipv4(ip, debug=False):

    octets = ip.split(".")
    colors = [convert_term_to_rgb(int(i)) for i in octets]

    width = 1024
    height = 1024

    im = Image.new(mode="RGB", size=(width, height), color="#ffffff")
    pixels = im.load()
    for x in range(width):
        for y in range(height):
            if x < 0x200 and y < 0x200:
                pixels[x, y] = colors[0]
            elif x < 0x400 and y < 0x200:
                pixels[x, y] = colors[1]
            elif x < 0x200 and y < 0x400:
                pixels[x, y] = colors[2]
            elif x < 0x400 and y < 0x400:
                pixels[x, y] = colors[3]
            else:
                pixels[x, y] = (0xFF, 0xFF, 0xFF)

    if debug:
        im.show()

    im.save(os.getcwd() + "/ip.png")
    sys.exit(0)
