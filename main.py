#!/usr/bin/python3
# -*- coding: utf-8 -*-

import signal
import sys
import logging
import tornado
from server.webserver import WebServer

def signal_handler(signal, frame):
  sys.exit(0)

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
    signal.signal(signal.SIGINT, signal_handler)
    WebServer().serve()
    tornado.ioloop.IOLoop.current().start()