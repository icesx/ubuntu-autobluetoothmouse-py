#!/bin/python
# coding=utf-8
'''
Created on 2014年4月19日

@author: i
'''
import os
import time
import sys
import log4py.log4py as log4py
class blutooth_mouse:
    mouse_name = "Logitech Bluetooth Wireless Mouse"
    def __init__(self):
        self.logger = log4py.Logger().get_instance(self)
        self.hidd_server()
        self.check_blutooth_mouse()
        self.logger.info("start all......")
        self.logger.info("sys exit!")
        sys.exit()
    def check_blutooth_mouse(self):
        while True:
            if self.ismouse_on() == True:
                self.logger.info("mouse is on")
                break
            else:
                self.hidd_search();
                time.sleep(3)
    def hidd_server(self):
        os.system("hidd --server")
        self.logger.info("hidd server started")
    def hidd_search(self):
        search_result = os.popen("hidd --search").read()
        self.logger.info("search result is " + search_result)
        self.logger.info(search_result)
    @staticmethod
    def ismouse_on():
        mouse_status = os.popen("xinput --list").read()
        if blutooth_mouse.mouse_name in mouse_status:
            return True
        else:
            return False
if __name__ == "__main__":
    blutooth_mouse()
