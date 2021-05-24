from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import wave
import threading
from os import remove,mkdir,listdir
from os.path import exists,splitext,basename,join
from datetime import datetime
from time import sleep
from shutil import rmtree
import pyaudio
# from PIL import ImageGrab
from PIL import Image
from moviepy.editor import *
import cv2
import numpy as np
import pyautogui
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import math
import statistics 
import sys
import time

barrier = threading.Event()

def open_youtube():
    print("START BROWSER")
    driver = webdriver.Firefox(executable_path='/home/lavinia/geckodriver')

    driver.get('https://www.youtube.com')

    search = driver.find_elements_by_class_name("lssxud")
    search[1].click()


    video = driver.find_elements_by_class_name("ytd-rich-item-renderer")
    sleep(7)
    video[0].click()

    barrier.set()

    while True:
        sleep(7)
        try:
            ads = driver.find_element_by_class_name("ytp-ad-skip-button")
            ads.click()
        except:
            break

    print("ASTEAPTA IN BROWSER")

    sleep(30)

    driver.quit()
    print("A IESIT DIN BROWSER")


def power(my_list):
    return [ x**2 for x in my_list ]


def record_audio():
    print("START RECORD AUDIO")
    # the file name output you want to record into
    filename = "recorded.wav"
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 2
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = 30
    # initialize PyAudio object
    p = pyaudio.PyAudio()

    barrier.wait()

    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        
        # my_audio_data = np.fromstring(data, dtype=np.short)
        # print(my_audio_data)

        # if you want to hear your voice while recording
        # stream.write(data)
        frames.append(data)
    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()

    print("FINAL AUDIO")

    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()
    print("FINAL SAVE AUDIO")

    # spf = wave.open(filename, "r")
    # Extract Raw Audio from Wav File
    # signal = spf.readframes(-1)
    # signal = np.fromstring(signal, "Int16")
    # fs = spf.getframerate()

    # # # If Stereo
    # # if spf.getnchannels() == 2:
    # #     print("Just mono files")
    # #     sys.exit(0)


    # Time = np.linspace(0, len(signal) / fs, num=len(signal))

    # plt.figure(1)
    # plt.title("Signal Wave...")
    # plt.plot(Time, signal)
    # plt.show()

    # p= pyaudio.PyAudio()
    # # event.wait()
    # sleep(3)
    # stream = p.open(format=FORMAT,
    #                 channels=CHANNELS,
    #                 rate=RATE,
    #                 input=True,
    #                 input_device_index=4,#3D mixing, which one to choose according to your needs
    #                 frames_per_buffer = CHUNK_sIZE)
    # wf = wave.open(audio_filename,'wb')
    # wf.setnchannels(CHANNELS)
    # wf.setsampwidth(p.get_sample_size(FORMAT))
    # wf.setframerate(RATE)
    # while allowRecording:
    #     # Read data from the recording device and write directly to the wav file
    #     data = stream.read(CHUNK_sIZE)
    #     wf.writeframes(data)
    # wf.close()
    # stream.stop_stream()
    # stream.close()
    # p.terminate()

def record_screen():
    print("START SCREEN")
    CHUNK_sIZE = 1024
    CHANNELS = 2
    FORMAT = pyaudio.paInt16
    RATE = 48000
    allowRecording = True
    SCREEN_SIZE = pyautogui.size()
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # create the video write object
    out = cv2.VideoWriter("output.avi", fourcc, 2.0, (SCREEN_SIZE))

    barrier.wait()

    old_minut = time.gmtime()[4] * 60 + time.gmtime()[5]

    frames = 0

    # max 30sec
    def minutePassed(oldminute):
        currentminute = time.gmtime()[4] * 60 + time.gmtime()[5]

        if ((currentminute - oldminute) >= 30):
            return True
        else:
            return False
    
    
    while True:
        frames = frames + 1
        if minutePassed(old_minut):
            break
        # make a screenshot
        img = pyautogui.screenshot()
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        out.write(frame)

        # # show the frame
        # cv2.imshow("screenshot", frame)

        # if the user clicks q, it exits
        
        # if cv2.waitKey(1) == ord("q"):
        #     break

    global fpss
    fpss = frames / 30
    print("FRAMES")
    print(frames)

    print("FINAL FOR SCREEN")
    # make sure everything is closed when exited
    cv2.destroyAllWindows()
    out.release()



now = str(datetime.now())[:19].replace(':','_')
audio_filename = "recorded.wav"
screen_video_filename = "output.avi"
video_filename = "%s.avi"%now

#Create two threads, recording and screen recording respectively

t3 = threading.Thread(target=open_youtube)

t1 = threading.Thread(target=record_audio)
t2 = threading.Thread(target=record_screen)


event = threading.Event()
event.clear()
for t in (t3,t1,t2):
    t.start()


# Wait for the camera to be secured, and prompt the user to start recording in three seconds

# event.wait(30)
print('Start recording after 3 seconds, press q to end recording')

for i in (t3,t1,t2):
    i.join()


#Combine the recorded video and audio into a video file
audio = AudioFileClip(audio_filename)

# DEBUG
print("DEBUG")
print('AUDIO DUR: ')
print(audio.duration)

video1 = VideoFileClip(screen_video_filename)


print('VIDEO DUR: ')
print(video1.duration)
print("FPSS")
print(fpss)

ratio1 = audio.duration / video1.duration
video1 = (video1.fl_time(lambda t: t/ratio1,apply_to=['video'])\
            .set_end(audio.duration))
            
video = CompositeVideoClip([video1]).set_audio(audio)
video.write_videofile(video_filename,codec= 'libx264',fps = fpss)

# remove(audio_filename)
remove(screen_video_filename)





