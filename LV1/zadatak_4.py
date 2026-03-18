'''
Napišite program koji od korisnika zahtijeva unos imena tekstualne datoteke. Program nakon toga treba tražiti linije oblika:
X-DSPAM-Confidence: <neki_broj>
koje predstavljaju pouzdanost korištenog spam filtra. Potrebno je izračunati srednju vrijednost pouzdanosti. 
Koristite datoteke mbox.txt i mbox-short.

Primjer
Ime datoteke: mbox.txt
Average X-DSPAM-Confidence: 0.894128046745
Ime datoteke: mbox-short.txt
Average X-DSPAM-Confidence: 0.750718518519
'''

naziv = input("Ime datoteke: ")

try:
    file = open(naziv)
except:
    print("Datoteka se ne može otvoriti.")
    quit()

broj = 0
ukupno = 0.0

for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        dijelovi = line.split(":")
        vrijednost = float(dijelovi[1])
        ukupno += vrijednost
        broj += 1


if broj > 0:
    average = ukupno / broj
    print("Average X-DSPAM-Confidence:", average)
else:
    print("Nema podataka.")

