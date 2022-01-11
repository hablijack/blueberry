#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import asyncio
import time


class Eyes():

    def __init__(self):
        self.logger = logging.getLogger("EYES")
        self.logger.info("Initializing Eyes Socket ...")

    async def off(self):
        self.logger.info('Set Eyes Off ...')

    async def twinkle(self):
        self.logger.info('Twinkle once ...')

    async def center(self):
        self.logger.info("Looking normal ...")

    async def right(self):
        self.logger.info("Looking right ...")

    async def left(self):
        self.logger.info("Looking left ...")

    async def angry(self):
        self.logger.info("Looking angry ...")

    async def sad(self):
        self.logger.info("Looking sad ...")

    async def wide(self):
        self.logger.info("Eyes wide open ...")

    async def eyes_googly(self):
        self.logger.info("Eyes googly ...")

    async def narrow(self):
        self.logger.info("Eyes narrow ...")

    async def exed(self):
        self.logger.info("Eyes xjiggle ...")
