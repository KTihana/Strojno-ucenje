'''
Napišite funkciju koja kao povratnu vrijednost daje sliku (polje) sa crno bijelim kvadratima jednake dimenzije koji se naizmjenično pojavljuju (vidi primjer slike ispod). 
Funkcija kao argumente prima veličinu kvadrata u pikselima, broj kvadrata po visini i broj kvadrata po širini slike. 
Za realizaciju ove funkcije koristite numpy funkcije zeros i ones kako biste kreirali crna i bijela polja. 
Kako bise ih složili u odgovarajući oblik koristite numpy funkcije hstack i vstack. Za prikaz grayscale slike koristite naredbu:
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
'''

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
