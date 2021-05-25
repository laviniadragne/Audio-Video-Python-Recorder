from __future__ import print_function
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf

# Analizeaza intr-o lista decibelii
fs_rate, signal = wavfile.read("recorded.wav")
chunk_size = 44100
num_chunk  = len(signal) // chunk_size
sn = []
for chunk in range(0, num_chunk):
  sn.append(np.mean(signal[chunk*chunk_size:(chunk+1)*chunk_size]**2))

print(sn)

logsn = 10*np.log10(sn)

print(logsn)

