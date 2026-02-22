"""
TP1 - Exercice 1
Génération d'un signal sinusoïdal
"""

import numpy as np
import matplotlib.pyplot as plt

# Paramètres
f0 = 10        # fréquence en Hz
A = 1          # amplitude
phi = 0        # phase
fs = 100       # fréquence d'échantillonnage
T = 1          # durée en secondes

# Création du vecteur temps
t = np.arange(0, T, 1/fs)

# Génération du signal
x = A * np.sin(2*np.pi*f0*t + phi)

# Affichage
plt.plot(t, x)
plt.title("Signal sinusoïdal 10 Hz")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()