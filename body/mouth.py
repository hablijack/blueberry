#!/usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import logging


class Mouth():
    def __init__(self):
        self.logger = logging.getLogger("MOUTH")

    async def mouth_open(self):
        self.logger.info("Open up mouth...")

    async def mouth_close(self):
        self.logger.info("Close mouth ...")
