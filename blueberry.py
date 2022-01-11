#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import time
import random
import asyncio
from body.voice import Voice
from body.eyes import Eyes
from body.mouth import Mouth


class Blueberry():

    operation_mode = 'INDEPENDANT'

    def __init__(self, operation_mode="INDEPENDANT"):
        self.logger = logging.getLogger('BLUEBERRY')
        self.operation_mode = operation_mode
        self.mouth = Mouth()
        self.eyes = Eyes()
        self.voice = Voice(self.mouth)

    async def alife(self):
        self.logger.info('Initializing the BLUEBERRY system, press Ctrl-C to quit...')
        await self.awake()
        independant_start = time.time()
        await self.random_idle(60.0, 120.0)
        while True:
            self.logger.info('Operation-Mode is: ' + self.operation_mode)
            if self.operation_mode == 'INDEPENDANT':
                if time.time() - independant_start > 500:
                    self.operation_mode = 'SLEEP'
                    self.logger.info('Setting Operation-Mode to: ' + self.operation_mode)
                else:
                    await self.random()
            elif self.operation_mode == 'SLEEP':
                self.sleep()
            await self.random_idle(60.0, 120.0)

    async def random_idle(self, min_idle, max_idle):
        self.logger.info('Going to idle mode ...')
        rand_idle = random.uniform(min_idle, max_idle)
        run_count = rand_idle / 6.0
        current_run=1
        while current_run <= run_count:
            await asyncio.sleep(random.uniform(3.0, 7.0))
            await self.eyes.twinkle()
            current_run+=1

    async def sad(self):
        self.logger.info('This is not good! Getting sad ...')
        await asyncio.gather(self.eyes.sad(), self.voice.sad())

    async def angry(self):
        self.logger.info('This is evil! Getting angry ...')
        await asyncio.gather(self.voice.nada(), self.eyes.angry() )

    async def smile(self):
        self.logger.info('Smiling for you ...')
        await asyncio.gather(self.voice.jiggle())

    async def laugh(self):
        self.logger.info('Funny things happened - laughing out loud ...')
        await asyncio.gather(self.voice.laugh())

    async def sleep(self):
        self.logger.info('Getting tired, going to sleep ...')
        await asyncio.gather(
            self.voice.yawn(),
            self.eyes.off(),
        )

    async def awake(self):
        self.logger.info('Awaken Furby...')
        await asyncio.gather(
            self.voice.yawn(),
            self.eyes.wide(),
        )
        await asyncio.sleep(random.uniform(1.0,2.0))
        await self.eyes.left()
        await asyncio.sleep(random.uniform(1.0,2.0))
        await self.eyes.right()
        await asyncio.sleep(random.uniform(1.0,2.0))
        await asyncio.gather( self.eyes.center() )

    async def random(self):
        self.logger.info('Doing random stuff ...')
        r = random.randint(1,4)
        if r == 1:
            await self.laugh()
        elif r == 2:
            await self.sad()
        elif r == 3:
            await self.smile()
        elif r == 4:
            await self.angry()
