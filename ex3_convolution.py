"""
TP1 - Exercice 3
Convolution d'un signal porte
"""

import numpy as np
import matplotlib.pyplot as plt

# Création du signal porte
rect = np.zeros(100)
rect[20:40] = 1

# Convolution du signal avec lui-même
conv = np.convolve(rect, rect)

# Affichage
plt.plot(conv)
plt.title("Convolution d'une porte avec elle-même")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()
plt.show()