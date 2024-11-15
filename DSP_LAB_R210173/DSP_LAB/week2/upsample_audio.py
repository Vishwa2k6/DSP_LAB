from scipy.io import wavfile
import numpy as np

fs, x = wavfile.read('/home/vishwanath/Desktop/DSP_LAB_R210173/DSP_LAB/WEEK2(24_7_24)/whisper-trail-2ogg-14429.wav')

def upsampling(x1, a):
    if a > 1:
        
        y = np.zeros((len(x1) * a, x1.shape[1])) 
        y[::a] = x1
        wavfile.write('/home/vishwanath/Desktop/DSP_LAB_R210173/DSP_LAB/WEEK2(24_7_24)/upsampled.wav', fs, y)

a = int(input("Enter upsampling factor: "))
upsampling(x, a)
