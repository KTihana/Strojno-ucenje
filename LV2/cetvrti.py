import numpy as np
import matplotlib.pyplot as plt

def sahovnica(velicina_kvadrata, broj_visina, broj_sirina):
    
    crni = np.zeros((velicina_kvadrata, velicina_kvadrata))
    bijeli = np.ones((velicina_kvadrata, velicina_kvadrata)) * 255

    redovi = []

    for i in range(broj_visina):
        red = []
        for j in range(broj_sirina):
            if (i + j) % 2 == 0:
                red.append(crni)   # crni gore lijevo
            else:
                red.append(bijeli)

        redovi.append(np.hstack(red))

    return np.vstack(redovi)


img = sahovnica(50, 4, 5)

plt.figure()
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title("Sahovnica 5x4")
plt.show()