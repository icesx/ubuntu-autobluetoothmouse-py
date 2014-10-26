#!/bin/python
# coding=utf-8
'''
Created on 2014年4月19日

@author: i
'''
import os
import time
import subprocess as sub
import log4py.log4py as log4py
logger = log4py.Logger().get_instance()
class blutooth_mouse:
    mouse_addr = "00:1F:20:D4:D8:59"
    def __init__(self):
        logger.info("starte all......")
        #self.hidd_server()
        self.times=0
        self.check_blutooth_mouse()
        logger.info("started all......")
    def check_blutooth_mouse(self):
        while self.times<10:
            if self.ismouse_on() == True:
                logger.info("mouse is on")
                break
            else:
                self.hidd_connect()
                time.sleep(3)
                self.times+=1
    def hidd_server(self):
        os.system("hidd --server")
        logger.info("hidd server started")
    def hidd_connect(self):
        cmd = "hidd --connect 00:1F:20:D4:D8:59" 
        p = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
        p.wait()
        output = p.stdout.read()
        logger.info("search result is " + output)
    @staticmethod
    def ismouse_on(): 
        cmd = "hidd" 
        try:
            p = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
            mouse_status = p.communicate()[0].rstrip()
            logger.info("mouse_status is " + mouse_status);
            if blutooth_mouse.mouse_addr in mouse_status:
                logger.info("blutooth_mouse.mouse_addr in mouse_status is True");
                return True
            else:
                logger.info("blutooth_mouse.mouse_addr in mouse_status is False" );
                return False
        except:
            logger.info("error")
if __name__ == "__main__":
    blutooth_mouse()
