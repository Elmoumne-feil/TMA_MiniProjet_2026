"""
TP3 - Partie 1 : Audio et Repliement (Aliasing)
- Chargement d'un fichier audio WAV
- Sous-échantillonnage sauvage (1 échantillon sur 10)
- Comparaison de spectrogrammes
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

# 1) Charger un fichier audio (wav)
# Mets ton fichier dans le même dossier TP3 et change le nom ici
audio_path = "audio.wav"
fs, x = wavfile.read(audio_path)

# Si stéréo -> on prend un seul canal
if x.ndim > 1:
    x = x[:, 0]

# Normalisation (pour affichage)
x = x.astype(np.float32)
x = x / (np.max(np.abs(x)) + 1e-12)

# 2) Sous-échantillonnage sauvage: garder 1 échantillon sur 10
facteur = 10
x_sub = x[::facteur]
fs_sub = fs // facteur

print("fs original =", fs, "Hz")
print("fs sous-échantillonné =", fs_sub, "Hz")

# 3) Spectrogramme original
f1, t1, Sxx1 = spectrogram(x, fs=fs, nperseg=1024, noverlap=512)
# 4) Spectrogramme sous-échantillonné
f2, t2, Sxx2 = spectrogram(x_sub, fs=fs_sub, nperseg=1024, noverlap=512)

# Affichage
plt.figure()
plt.pcolormesh(t1, f1, 10*np.log10(Sxx1 + 1e-12), shading='auto')
plt.title("Spectrogramme - Signal original")
plt.xlabel("Temps (s)")
plt.ylabel("Fréquence (Hz)")
plt.ylim(0, 20000)
plt.colorbar(label="dB")
plt.show()

plt.figure()
plt.pcolormesh(t2, f2, 10*np.log10(Sxx2 + 1e-12), shading='auto')
plt.title("Spectrogramme - Signal sous-échantillonné (1/10)")
plt.xlabel("Temps (s)")
plt.ylabel("Fréquence (Hz)")
plt.ylim(0, 20000)
plt.colorbar(label="dB")
plt.show()

# Remarque: pour l'écoute, tu peux sauvegarder x_sub en wav (optionnel)
# wavfile.write("audio_sous.wav", fs_sub, (x_sub * 32767).astype(np.int16))