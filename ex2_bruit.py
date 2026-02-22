"""
TP1 - Exercice 2
Ajout de bruit blanc gaussien
"""

import numpy as np
import matplotlib.pyplot as plt

# Paramètres du signal
f0 = 10
A = 1
phi = 0
fs = 100
T = 1

# Création du vecteur temps
t = np.arange(0, T, 1/fs)

# Signal sinusoïdal
x = A * np.sin(2*np.pi*f0*t + phi)

# Génération du bruit blanc gaussien
bruit = np.random.normal(0, 0.3, len(x))

# Signal bruité
y = x + bruit

# Affichage
plt.plot(t, x, label="Signal pur")
plt.plot(t, y, label="Signal bruité")
plt.legend()
plt.title("Signal avec bruit blanc gaussien")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()