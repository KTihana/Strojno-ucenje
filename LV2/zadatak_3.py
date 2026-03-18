'''
Zadatak 3
Na temelju primjera 2.5. učitajte sliku 'tiger.png'. Manipulacijom odgovarajuće numpy matrice pokušajte:
a) posvijetliti sliku (povećati brightness),
b) zarotirati sliku za 90 stupnjeva u smjeru kazaljke na satu,
c) zrcaliti sliku,
d) smanjiti rezoluciju slike x puta (npr. 10 puta),
e) prikazati samo drugu četvrtinu slike po širini, a prikazati sliku cijelu po visini; ostali dijelovi slike trebaju biti crni.
'''


import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
img = img[:, :, 0].copy()

# a) Posvjetljenje slike
brightness = 50
bright = np.clip(img + brightness, 0, 255)

plt.figure()
plt.imshow(bright, cmap="gray")
plt.title("Posvjetljena slika")
plt.show()

# b) Rotacija 
rotated = np.rot90(img, k=-1)

plt.figure()
plt.imshow(rotated, cmap="gray")
plt.title("Rotirana slika")
plt.show()

# c) Zrcaljenje
mirrored = np.fliplr(img)

plt.figure()
plt.imshow(mirrored, cmap="gray")
plt.title("Zrcaljena slika")
plt.show()

# d) Smanjena rezolucija 
smanjenje = 10
small = img[::smanjenje, ::smanjenje]

plt.figure()
plt.imshow(small, cmap="gray")
plt.title("Manja rezolucija")
plt.show()

# e) Druga cetvrtina po sirini
h, w = img.shape
result = np.zeros_like(img)
result[:, w//4:w//2] = img[:, w//4:w//2]

plt.figure()
plt.imshow(result, cmap="gray")
plt.title("Druga četvrtina slike po širini")
plt.show()
