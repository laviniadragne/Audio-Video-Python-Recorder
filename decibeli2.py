from pydub import AudioSegment
import numpy as np
import soundfile as sfile
import math
import matplotlib.pyplot as plt

filename = 'recorded.wav'

audio=AudioSegment.from_mp3(filename)
signal, sr = sfile.read(filename)
samples=audio.get_array_of_samples()
samples_sf=0
try:
    samples_sf = signal[:, 0]  # use the first channel for dual
except:
    samples_sf=signal  # for mono


def convert_to_decibel(arr):
    ref = 1
    if arr!=0:
        return 20 * np.log10(abs(arr) / ref)
        
    else:
        return -60

data=[convert_to_decibel(i) for i in samples_sf]
percentile=np.percentile(data,[25,50,75])
print("1st Quartile: " + str({percentile[0]}))
print("2nd Quartile :" + str({percentile[1]}))
print("3rd Quartile :" + str({percentile[2]}))
print("Mean :" + str({np.mean(data)}))
print("Median :" + str({np.median(data)}))
print("Standard Deviation :" + str({np.std(data)}))
print("Variance :" + str({np.var(data)}))


plt.figure()
plt.plot(3, 1, 1)
plt.plot(data)
plt.xlabel('Samples')
plt.ylabel('dB Full Scale (dB)')
plt.tight_layout()
plt.show()