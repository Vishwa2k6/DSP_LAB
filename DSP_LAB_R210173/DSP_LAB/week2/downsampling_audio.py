
from scipy.io import wavfile

fs, x = wavfile.read('/home/vishwanath/Desktop/DSP_LAB_R210173/DSP_LAB/WEEK2(24_7_24)/whisper-trail-2ogg-14429.wav')


def sampling(x, a):
    if a > 1:
        y=x[::a]
        wavfile.write('/home/vishwanath/Desktop/DSP_LAB_R210173/DSP_LAB/WEEK2(24_7_24)/downsampled.wav',fs,y)


a=int(input("Enter sampling factor:"))
sampling(x, a)