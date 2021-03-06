#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tornado
from server.handler.homepage import Homepage
from tornado.web import Application
import os
import logging

rel = lambda *x: os.path.abspath(os.path.join(os.path.dirname(__file__), *x))


class WebServer():

    def __init__(self):
        self.logger = logging.getLogger('WEBSERVER')

    def serve(self):
        settings = dict(
            template_path=rel('./web/templates'),
            static_path=rel('./web'),
            debug=True
        )
        app = Application([
            (r"/", Homepage)
        ], **settings)

        http_server = tornado.httpserver.HTTPServer(app)
        port = '8080'
        http_server.listen(port=port)
        self.logger.info("... blueberry GUI is serving under 127.0.0.1:{}.".format(port))