# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os
sys.path.append('/home/spurs/darknet/python/')

import darknet as dn
import cv2
import socket
import numpy as np

'''
dn.set_gpu(0)
net = dn.load_net("/home/spurs/darknet/cfg/yolov3.cfg".encode('ascii'), "/home/spurs/darknet/yolov3.weights".encode('ascii'), 0)
meta = dn.load_meta("/home/spurs/darknet/cfg/coco.data".encode('ascii'))
'''

def show():

    dn.set_gpu(0)
    net = dn.load_net("/home/spurs/darknet/cfg/yolov3.cfg".encode('ascii'), "/home/spurs/darknet/yolov3.weights".encode('ascii'), 0)
    meta = dn.load_meta("/home/spurs/darknet/cfg/coco.data".encode('ascii'))
   
    src = '/home/spurs/camera/camera.jpg'
    while True:
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        try:
            frame = cv2.imread(src)
            cv2.imshow('frame', frame)
        except:
            continue
    
        cv2.imwrite('/home/spurs/camera/camera_1.jpg', frame)
        r = dn.detect(net, meta, "/home/spurs/camera/camera_1.jpg".encode('ascii'))
        for bb in r:
            x, y, w, h = bb[2]
            x_max = int(round((2*x+w)/2))
            x_min = int(round((2*x-w)/2))
            y_min = int(round((2*y-h)/2))
            y_max = int(round((2*y+h)/2))
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 255, 0), 2)
            cv2.putText(frame, bb[0].decode('utf-8'), (x_min, y_min-10), 2, 1, (255, 0, 255), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord ('q'):
            break

show()
'''
r = dn.detect(net, meta, "/home/spurs/darknet/data/dog.jpg".encode('ascii'))
print(r)

# And then down here you could detect a lot more images like:
r = dn.detect(net, meta, "/home/spurs/darknet/data/eagle.jpg".encode('ascii'))
print(r)
r = dn.detect(net, meta, "/home/spurs/darknet/data/giraffe.jpg".encode('ascii'))
print(r)
r = dn.detect(net, meta, "/home/spurs/darknet/data/horses.jpg".encode('ascii'))
print(r)
r = dn.detect(net, meta, "/home/spurs/darknet/data/person.jpg".encode('ascii'))
print(r)
'''
