#!/usr/bin/python

#Shane Miller, used pi forums, and Derek


import time

import os

import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)





import socket

import time

SERVERIP = '10.0.0.22'

n = 0 





while True: 

    state = GPIO.input(23)





    if (state == 0):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((SERVERIP, 8881))

        localtime = time.asctime( time.localtime(time.time()) )

        data = "ShaneMiller,%d, its raining %s" %(n, localtime)

        sock.sendall(data)

        sock.close( )

        time.sleep(5)

        n = n+1

        print " sent:", data







        print "its raining!", localtime

    else:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((SERVERIP, 8881))

        localtime = time.asctime( time.localtime(time.time()) )

        data = "ShaneMiller ,%d, No water %s" %(n, localtime)

        sock.sendall(data)

        sock.close( )

        time.sleep(5)

        n = n+1

        print "Its not raining", localtime

    time.sleep(21) 
