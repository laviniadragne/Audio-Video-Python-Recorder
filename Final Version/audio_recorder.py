import wave
import pyaudio
import numpy as np
from scipy.io.wavfile import read


# Singleton class
class AudioRecorder:

    __instance = None
    def getInstance(filename):
        if AudioRecorder.__instance == None:
            AudioRecorder(filename)
        return AudioRecorder.__instance


    def __init__(self, filename, chunk = 1024, channels = 2, sample_rate = 44100,
                my_format = pyaudio.paInt16, record_seconds = 120):
        if AudioRecorder.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AudioRecorder.__instance = self

        self.filename = filename
        self.chunk = chunk
        self.channels = channels
        self.sample_rate = sample_rate
        self.record_seconds = record_seconds
        self.format = my_format
        # initialize PyAudio object
        self.p = pyaudio.PyAudio()

    def open_stream(self):
         # open stream object as input & output
        self.stream = self.p.open(format = self.format,
                                channels = self.channels,
                                rate = self.sample_rate,
                                input = True,
                                output = True,
                                frames_per_buffer = self.chunk)


    def create_frames(self):
        self.frames = []
        print("Recording audio...")

        for i in range(int(self.sample_rate / self.chunk * self.record_seconds)):
            data = self.stream.read(self.chunk)
            self.frames.append(data)

        print("Finished recording audio.")

    def close_stream(self):
        # stop and close stream
        self.stream.stop_stream()
        self.stream.close()
        # terminate pyaudio object
        self.p.terminate()


    def write_frames(self):
         # open the file in 'write bytes' mode
        wf = wave.open(self.filename, "wb")
        # set the channels
        wf.setnchannels(self.channels)
        # set the sample format
        wf.setsampwidth(self.p.get_sample_size(self.format))
        # set the sample rate
        wf.setframerate(self.sample_rate)
        # write the frames as bytes
        wf.writeframes(b"".join(self.frames))
        # close the file
        wf.close()
        print("Save audio")

