"""
TP3 - Partie 2 : Image et Quantification
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# Option 1: OpenCV
import cv2

# --- 1) Charger l'image (png/jpg/jpeg) depuis le dossier courant ---
possible_names = ["image.png", "image.jpg", "image.jpeg"]
img = None
img_path_used = None

for name in possible_names:
    if os.path.exists(name):
        img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
        img_path_used = name
        break

if img is None:
    raise FileNotFoundError(
        "Image introuvable dans le dossier TP3.\n"
        "Mets ton image à côté du fichier .py et renomme-la image.png (ou image.jpg).\n"
        f"Dossier courant: {os.getcwd()}"
    )

print("Image chargée :", img_path_used, "| taille:", img.shape)

# --- 2) Quantification ---
# 4 niveaux (2 bits)
img_4 = (img // 64) * 64

# 2 niveaux (1 bit)
img_2 = (img // 128) * 128

# --- Affichage ---
plt.figure()
plt.imshow(img, cmap="gray")
plt.title("Image originale (8 bits - 256 niveaux)")
plt.axis("off")
plt.show()

plt.figure()
plt.imshow(img_4, cmap="gray")
plt.title("Quantification 2 bits (4 niveaux)")
plt.axis("off")
plt.show()

plt.figure()
plt.imshow(img_2, cmap="gray")
plt.title("Quantification 1 bit (2 niveaux)")
plt.axis("off")
plt.show()

# --- 3) Pixelisation ---
h, w = img.shape

# éviter erreur si image trop petite
new_w = max(1, w // 8)
new_h = max(1, h // 8)

img_small = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
img_pixel = cv2.resize(img_small, (w, h), interpolation=cv2.INTER_NEAREST)

plt.figure()
plt.imshow(img_pixel, cmap="gray")
plt.title("Pixelisation (réduction /8 puis agrandissement)")
plt.axis("off")
plt.show()