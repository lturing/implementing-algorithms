import sys, os
sys.path.append('/home/spurs/darknet/python/')

import darknet as dn
import numpy as np

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.escape import json_decode, json_encode
from uuid import uuid4
import base64
import cv2
import json

dn.set_gpu(0)
net = dn.load_net("/home/spurs/darknet/cfg/yolov3.cfg".encode('ascii'), "/home/spurs/darknet/yolov3.weights".encode('ascii'), 0)
meta = dn.load_meta("/home/spurs/darknet/cfg/coco.data".encode('ascii'))

class ShoppingCart(object):
    totalInventory = 10
    callbacks = []
    carts = {}

    def register(self, callback):
        self.callbacks.append(callback)

    def moveItemToCart(self, session):
        if session in self.carts:
            return

        self.carts[session] = True
        self.notifyCallbacks()

    def removeItemFromCart(self, session):
        if session not in self.carts:
            return

        del(self.carts[session])
        self.notifyCallbacks()

    def notifyCallbacks(self):
        for c in self.callbacks:
            self.callbackHelper(c)

        self.callbacks = []

    def callbackHelper(self, callback):
        callback(self.getInventoryCount())

    def getInventoryCount(self):
        return self.totalInventory - len(self.carts)

class openCameraHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("camera.html")

class DetailHandler(tornado.web.RequestHandler):
    def get(self):
        session = uuid4()
        count = self.application.shoppingCart.getInventoryCount()
        self.render("index.html", session=session, count=count)

class CartHandler(tornado.web.RequestHandler):
    def post(self):
        action = self.get_argument('action')
        session = self.get_argument('session')

        if not session:
            self.set_status(400)
            return

        if action == 'add':
            self.application.shoppingCart.moveItemToCart(session)
        elif action == 'remove':
            self.application.shoppingCart.removeItemFromCart(session)
        else:
            self.set_status(400)

class CameraHandler(tornado.web.RequestHandler):
    def post(self):
        data = json_decode(self.request.body)
        img = data['img']
        img = base64.b64decode(img)
        fpath = '/home/spurs/camera_new.jpg'
        f = open(fpath, 'wb')
        f.write(img)
        f.close()
        try:
            r = dn.detect(net, meta, fpath.encode('ascii'))
            frame = cv2.imread(fpath)
            for bb in r:
                x, y, w, h = bb[2]
                x_max = int(round((2*x+w)/2))
                x_min = int(round((2*x-w)/2))
                y_min = int(round((2*y-h)/2))
                y_max = int(round((2*y+h)/2))
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 255, 0), 2)
                cv2.putText(frame, bb[0].decode('utf-8'), (x_min, y_min-10), 2, 1, (255, 0, 255), 2)
                
            cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
            cv2.imshow('frame', frame)
            cv2.waitKey(1)
        except AssertionError as e:
            #raise
            pass
        
        #_thread.start_new_thread(play, ())
        '''
        image = cv2.imread('/home/hadoop/camera_new/camera.jpg')
        cv2.imshow('camera', image)
        cv2.waitKey(1) & 0xFF == ord ('q')
        '''


class StatusHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.application.shoppingCart.register(self.on_message)

    def on_message(self, count):
        self.write('{"inventoryCount":"%d"}' % count)
        self.finish()



class Application(tornado.web.Application):
    def __init__(self):
        self.shoppingCart = ShoppingCart()

        handlers = [
            (r'/', openCameraHandler),
            (r'/detail', DetailHandler),
            (r'/cart', CartHandler),
            (r'/cart/status', StatusHandler),
            (r'/camera', CameraHandler),
        ]

        settings = {
            'template_path': 'templates',
            'static_path': 'static'
        }

        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()

    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    print('10.5.1.49:9000')
    server.listen(9000)
    tornado.ioloop.IOLoop.instance().start()
