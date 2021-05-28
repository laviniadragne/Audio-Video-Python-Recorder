from pydub import AudioSegment
import numpy as np
import soundfile as sfile
import math
import matplotlib.pyplot as plt

class AudioAnalyzer:

    def __init__(self, filename):
        self.filename = filename
        self.audio = AudioSegment.from_mp3(self.filename)
        self.signal, self.sr = sfile.read(self.filename)
        self.samples = self.audio.get_array_of_samples()
        try:
            self.samples_sf = self.signal[:, 0]  # use the first channel for dual
        except:
            self.samples_sf = self.signal

   
    def convert_to_decibel(self, arr):
        ref = 1
        if arr != 0:
            return 20 * np.log10(abs(arr) / ref)
            
        else:
            return -60

    def create_percentile(self):
        self.data = [self.convert_to_decibel(i) for i in self.samples_sf]
        # Calculate the line of the samples in the graphic
        percentile = np.percentile(self.data, [25, 50, 75])


    def figure_plot(self):
        plt.figure()
        plt.plot(3, 1, 1)
        plt.plot(self.data)
        plt.xlabel('Samples')
        plt.ylabel('dB Full Scale (dB)')
        plt.tight_layout()
        plt.show()