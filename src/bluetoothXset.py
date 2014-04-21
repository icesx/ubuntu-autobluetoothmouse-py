#!/bin/python
# coding=utf-8
'''
Created on 2014年4月19日

@author: i
'''
import os
import time
import sys
from bluetoothMouseAutoCon import blutooth_mouse
import log4py.log4py as log4py
logger = log4py.Logger().get_instance()
while True:
    if blutooth_mouse.ismouse_on() == True:
        os.system("xset m 2 10")
        logger.info("xset m 2 10 is ok!")
        sys.exit(0)
    else:
        time.sleep(3);
    
