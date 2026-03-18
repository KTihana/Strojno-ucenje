'''
Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. 
Potrebno je napraviti rječnik koji kao ključeve koristi sve različite riječi koje se pojavljuju u datoteci, 
dok su vrijednosti jednake broju puta koliko se svaka riječ (ključ) pojavljuje u datoteci. 
Koliko je riječi koje se pojavljuju samo jednom u datoteci? Ispišite ih.
'''


naziv_datoteke = "song.txt"
datoteka = open(naziv_datoteke)
broj_rijeci = {}

for linija in datoteka:
    rijeci = linija.split()
    for rijec in rijeci:
        if rijec in broj_rijeci:
            broj_rijeci[rijec] += 1
        else:
            broj_rijeci[rijec] = 1

datoteka.close()

jedno_ponavljanje = []

for rijec in broj_rijeci:
    if broj_rijeci[rijec] == 1:
        jedno_ponavljanje.append(rijec)

print("Riječi koje se pojavljuju samo jednom:")
for rijec in jedno_ponavljanje:
    print(rijec)

print("Broj rijeci:", len(jedno_ponavljanje))
