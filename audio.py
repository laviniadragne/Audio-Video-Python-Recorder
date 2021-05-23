import pyaudio
import numpy as np
import pyautogui
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import math
import statistics 
import sys

def power(my_list):
    return [ x**2 for x in my_list ]

filename = "recorded.wav"
samprate, wavdata = read(filename)
    # basically taking a reading every half a second - the size of the data 
    # divided by the sample rate gives us 1 second chunks so I chop 
    # sample rate in half for half second chunks
chunks = np.array_split(wavdata, wavdata.size/(samprate/2))
# for chu in chunks: 
#     print((chu.flatten()).flatten())
dbs = [20*math.log10(math.sqrt(statistics.mean(power(chu.flatten())))) for chu in chunks]
print(dbs)
