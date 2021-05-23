import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import scipy.fftpack as fft
plt.close('all')

fs=44100
duration=5
print("recording...............")


record_voice=sd.rec(int(duration * fs),samplerate=fs,channels=2)
sd.wait()       
write("sound.wav",fs,record_voice)

#Play
# sd.play(record_voice, fs)
plt.plot(record_voice); plt.title("Recorded sound")
plt.show()

