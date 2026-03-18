'''
U direktoriju PSU_LV/LV2/ nalazi se datoteka mtcars.csv koja sadrži različita mjerenja provedena na 32 automobila (modeli 1973-74). Opis pojedinih varijabli nalazi se u datoteci mtcars_info.txt.
a) Učitajte datoteku mtcars.csv pomoću:
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
b) Prikažite ovisnost potrošnje automobila (mpg) o konjskim snagama (hp) pomoću naredbe matplotlib.pyplot.scatter.
c) Na istom grafu prikažite i informaciju o težini pojedinog vozila (npr. veličina točkice neka bude u skladu sa težinom wt).
d) Izračunajte minimalne, maksimalne i srednje vrijednosti potrošnje (mpg) automobila.
e) Ponovite zadatak pod d), ali samo za automobile sa 6 cilindara (cyl).
'''

import numpy as np
import matplotlib.pyplot as plt
 
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
 
mpg = data[:, 0]
hp  = data[:, 3]
wt  = data[:, 5] 
 
plt.scatter(hp,mpg,s=wt*25)
plt.xlabel("Konjska snaga (hp)")
plt.ylabel('Potrošnja (mpg)')
plt.title('Ovisnost potrošnje o snazi i težini')
plt.show()
 
print("\nSvi automobili MPG:")
print("Max:", mpg.max())
print("Min:", mpg.min())
print("Mean:", mpg.mean())
 
mpg_6cyl = []
 
for i in range(0,32):
    if data[i,1] == 6:
        mpg_6cyl.append(data[i, 0])
 
mpg_6cyl = np.array(mpg_6cyl)
 
print("\nG-cilindrični automobili MPG:")
print("Max:", mpg_6cyl.max())
print("Min:", mpg_6cyl.min())
print("Mean:", mpg_6cyl.mean())
 
