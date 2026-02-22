"""
TP2 - Exercice 2
Ajout d'un bruit et filtrage par FFT
"""

import numpy as np
import matplotlib.pyplot as plt

# Paramètres
fs = 44100
T = 1
t = np.arange(0, T, 1/fs)

f1 = 440
f2 = 880
f_bruit = 5000

# Signal original
signal = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)

# Ajout bruit haute fréquence
bruit = 0.3 * np.sin(2*np.pi*f_bruit*t)
signal_bruite = signal + bruit

# FFT
fft_signal = np.fft.fft(signal_bruite)
freq = np.fft.fftfreq(len(signal_bruite), 1/fs)

# Filtrage simple : suppression autour de 5000 Hz
mask = (np.abs(freq - f_bruit) < 50)
fft_signal[mask] = 0

# Reconstruction
signal_filtre = np.fft.ifft(fft_signal)

# Affichage
plt.plot(t[:1000], signal_bruite[:1000], label="Signal bruité")
plt.plot(t[:1000], signal_filtre[:1000].real, label="Signal filtré")
plt.legend()
plt.title("Filtrage du bruit")
plt.show()