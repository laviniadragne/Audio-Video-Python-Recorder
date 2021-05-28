from time import sleep
import threading
from datetime import datetime
import pyaudio
from moviepy.editor import *
import cv2
import numpy as np
import pyautogui
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import math
import sys
import time
from browser_opener import BrowserOpener
from audio_recorder import AudioRecorder
from screen_recorder import ScreenRecorder
from audio_analyzer import  AudioAnalyzer

barrier = threading.Event()
    
def open_browser():
    opener = BrowserOpener('/home/lavinia/geckodriver', 'https://www.youtube.com')

    opener.get_driver()
    opener.open_url('lssxud')
    opener.play_video('ytd-rich-item-renderer')

    # Thread synchronization
    barrier.set()

    opener.skip_ads('ytp-ad-skip-button')
    sleep(120)

    opener.close()

def record_audio():
    recorder = AudioRecorder('recorded.wav')

    barrier.wait()

    recorder.open_stream()
    recorder.create_frames()
    recorder.close_stream()
    recorder.write_frames()
    

def record_screen():
    recorder = ScreenRecorder('output.avi', 14.0)

    barrier.wait()

    old_minut = time.gmtime()[4] * 60 + time.gmtime()[5]
    recorder.create_frame(old_minut, 120)

    recorder.close_out()


def create_video(audio_filename, screen_video_filename):
    audio = AudioFileClip(audio_filename)
    video_file = VideoFileClip(screen_video_filename)

    ratio1 = audio.duration / video_file.duration
    video1 = (video_file.fl_time(lambda t: t/ratio1, apply_to=['video'])\
                .set_end(audio.duration))
                
    video = CompositeVideoClip([video_file]).set_audio(audio)
    video.write_videofile(video_filename, codec= 'libx264', fps = 14)


def audio_analyze():
    analyzer = AudioAnalyzer('recorded.wav')
    analyzer.create_percentile()
    analyzer.figure_plot()


# Create three threads, open browser, recording audio and screen
t3 = threading.Thread(target=open_browser)
t1 = threading.Thread(target=record_audio)
t2 = threading.Thread(target=record_screen)

# Start threads
for t in (t3, t1, t2):
    t.start()

print('Start recording maximum 2 minutes')

# Thread goes into a waiting state
for i in (t3, t1, t2):
    i.join()


# Create name for video
now = str(datetime.now())[:19].replace(':','_')
video_filename = "%s.avi"%now

# Combine the recorded video and audio into a video file
create_video('recorded.wav', 'output.avi')

# Analize the audio
audio_analyze()




