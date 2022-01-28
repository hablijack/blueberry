#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import tornado
from server.webserver import WebServer
from blueberry import Blueberry

if __name__ in '__main__':

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s [%(name)s] %(message)s",
        datefmt='%d.%m.%Y %H:%M:%S',
        handlers=[
            logging.FileHandler("log/debug.log"),
            logging.StreamHandler()
        ]
    )
    blueberry = Blueberry()
    blueberry.wakeup()
    WebServer(blueberry).serve()
    tornado.ioloop.IOLoop.current().start()
