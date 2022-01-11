#!/usr/bin/python3
# -*- coding: utf-8 -*-

from helper.sound_player import SoundPlayer
import sys
import logging
import random
import asyncio
import time


class Voice:

    def __init__(self, mouth):
        self.logger = logging.getLogger('VOICE')
        self.player = SoundPlayer()
        self.mouth = mouth

    async def sad(self):
        await self.mouth.mouth_open()
        self.logger.info('Trying to play sad.wav file.')
        await self.player.play("sounds/sad.wav")
        self.logger.info('Done playing sad.wav file.')
        await self.mouth.mouth_close()

    async def notification(self):
        await self.mouth.mouth_open()
        self.logger.info('Trying to play notification.wav file.')
        await self.player.play("sounds/notification.wav")
        self.logger.info('Done playing notification.wav file.')
        await self.mouth.mouth_close()

    async def nada(self):
        await self.mouth.mouth_open()
        self.logger.info('Trying to play nada.wav file.')
        await self.player.play("sounds/nada.wav")
        self.logger.info('Done playing nada.wav file.')
        await self.mouth.mouth_close()

    async def kakadududu(self):
        await self.mouth.mouth_open()
        self.logger.info('Trying to play kakadududu.wav file.')
        await self.player.play("sounds/kakadududu.wav")
        self.logger.info('Done playing kakadududu.wav file.')
        await self.mouth.mouth_close()

    async def jiggle(self):
        await self.mouth.mouth_open()
        self.logger.info('Trying to play jiggle.wav file.')
        await self.player.play("sounds/jiggle.wav")
        self.logger.info('Done playing jiggle.wav file.')
        await self.mouth.mouth_close()

    async def yawn(self):
        await self.mouth.mouth_open()
        self.logger.info('Trying to play yawn.wav file.')
        await self.player.play("sounds/yawn.wav")
        self.logger.info('Done playing yawn.wav file.')
        await self.mouth.mouth_close()

    async def laugh(self):
        await self.mouth.mouth_open()
        self.logger.info('Trying to play laugh.wav file.')
        await self.player.play("sounds/laugh.wav")
        self.logger.info('Done playing laugh.wav')
        await self.mouth.mouth_close()
