"""
TP2 - Exercice 1
Analyse spectrale d'un signal audio
"""

import numpy as np
import matplotlib.pyplot as plt

# Paramètres
fs = 44100
T = 1
t = np.arange(0, T, 1/fs)

f1 = 440
f2 = 880

# Signal composé
signal = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)

# FFT
fft_signal = np.fft.fft(signal)
freq = np.fft.fftfreq(len(signal), 1/fs)

# Module FFT
plt.plot(freq, np.abs(fft_signal))
plt.xlim(0, 2000)
plt.title("Spectre du signal")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()