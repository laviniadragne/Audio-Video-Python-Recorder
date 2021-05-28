from moviepy.editor import *
import cv2
import numpy as np
import pyautogui
import pyaudio
from datetime import datetime
import sys
import time
from time import sleep

class ScreenRecorder:
    def __init__(self, filename, frames, chunk = 1024, channels = 2, rate = 48000,
                my_format = pyaudio.paInt16):
        self.filename = filename
        self.screen_size = pyautogui.size()
        self.chunk = chunk
        self.channels = channels
        self.rate = rate
        self.format = my_format
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.out = cv2.VideoWriter(self.filename, self.fourcc, frames, self.screen_size)

    # If passed 120 seconds
    def minute_passed(self, oldminute, record_seconds):
        currentminute = time.gmtime()[4] * 60 + time.gmtime()[5]

        if ((currentminute - oldminute) >= record_seconds):
            return True
        else:
            return False


    def create_frame(self, old_minut, record_seconds):
        print('Recording screen')
        while True:
            if self.minute_passed(old_minut, record_seconds):
                break
            # make a screenshot
            img = pyautogui.screenshot()
            # convert these pixels to a proper numpy array to work with OpenCV
            frame = np.array(img)
            # convert colors from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # write the frame
            self.out.write(frame)


    def close_out(self):
        print('Save screen record')
         # make sure everything is closed when exited
        cv2.destroyAllWindows()
        self.out.release()