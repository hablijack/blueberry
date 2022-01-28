#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from tornado import gen
from eventsource.speech_recognition import SpeechRecognition

class Blueberry():

    def __init__(self):
        self.logger = logging.getLogger('BLUEBERRY')
        self.logger.debug('... initializing blueberry system, press Ctrl-C to quit!')
        self.start_speech_recognition()

    @gen.coroutine
    def start_speech_recognition(self):
        self.logger.debug('... waking speech recognition coroutines to sense spoken words!')
        SpeechRecognition().run()
