import netaddr, sys, os
from PIL import Image
from .util import *


def _ipv6(ip, debug):
    ip = netaddr.IPAddress(ip)
    hextets = ip.format(dialect=netaddr.ipv6_verbose).split(":")
    hex_array = []
    for hextet in hextets:
        hex_array.append(hextet[0:2])
        hex_array.append(hextet[2:])
    int_array = [int(i, 16) for i in hex_array]

    colors = []
    for i in int_array:
        colors.append(convert_term_to_rgb(i))

    width = 1024
    height = 1024

    im = Image.new(mode="RGB", size=(width, height), color="#ffffff")
    pixels = im.load()
    for x in range(width):
        for y in range(height):
            if x < 0x100 and y < 0x100:
                pixels[x, y] = colors[0]
            elif x < 0x200 and y < 0x100:
                pixels[x, y] = colors[1]
            elif x < 0x300 and y < 0x100:
                pixels[x, y] = colors[2]
            elif x < 0x400 and y < 0x100:
                pixels[x, y] = colors[3]
            elif x < 0x100 and y < 0x200:
                pixels[x, y] = colors[4]
            elif x < 0x200 and y < 0x200:
                pixels[x, y] = colors[5]
            elif x < 0x300 and y < 0x200:
                pixels[x, y] = colors[6]
            elif x < 0x400 and y < 0x200:
                pixels[x, y] = colors[7]
            elif x < 0x100 and y < 0x300:
                pixels[x, y] = colors[8]
            elif x < 0x200 and y < 0x300:
                pixels[x, y] = colors[9]
            elif x < 0x300 and y < 0x300:
                pixels[x, y] = colors[10]
            elif x < 0x400 and y < 0x300:
                pixels[x, y] = colors[11]
            elif x < 0x100 and y < 0x400:
                pixels[x, y] = colors[12]
            elif x < 0x200 and y < 0x400:
                pixels[x, y] = colors[13]
            elif x < 0x300 and y < 0x400:
                pixels[x, y] = colors[14]
            elif x < 0x400 and y < 0x400:
                pixels[x, y] = colors[15]
            else:
                pixels[x, y] = (0xFF, 0xFF, 0xFF)

    if debug:
        im.show()

    im.save(os.getcwd() + "/ip.png")
    sys.exit(0)
