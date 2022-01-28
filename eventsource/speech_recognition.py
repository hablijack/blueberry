import os
import struct
import wave
from datetime import datetime
from threading import Thread

import pvporcupine
from pvrecorder import PvRecorder

class SpeechRecognition(Thread):

    def __init__(self):
        super(SpeechRecognition, self).__init__()

    def run(self):
        porcupine = None
        recorder = None
        wav_file = None
        try:
            porcupine = pvporcupine.create(
                access_key="cfVaAleMzTRcsV/T/boeRxI1ZH4QI1CiiEgw21FJhA8vw6wEB8+dOA==",
                library_path=pvporcupine.LIBRARY_PATH,
                model_path=pvporcupine.MODEL_PATH,
                keywords=["blueberry"])

            recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
            recorder.start()

            while True:
                if porcupine.process(recorder.read()) >= 0:
                    print("detected")
        except Exception as e:
            print(e)
        finally:
            if porcupine is not None:
                porcupine.delete()

            if recorder is not None:
                recorder.delete()

            if wav_file is not None:
                wav_file.close()

