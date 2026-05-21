#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import epd2in9bc
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import time

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in9bc Demo")

    epd = epd2in9bc.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    img = Image.open("qr.png").convert("1")
    time.sleep(1)


    # Drawing on the image


    print(f"The height is {epd.height}")
    print(f"The width is {epd.width}")

    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font30 = ImageFont.truetype(os.path.join(picdir, "Font.ttc"), 30)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

    # Drawing the image
    img = img.resize((epd.height, epd.width))

    blackimage = img

    redimage = Image.new("1", (epd.height, epd.width), 255)
    epd.display(epd.getbuffer(blackimage), epd.getbuffer(redimage))

    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in9bc.epdconfig.module_exit(cleanup=True)
    exit()
