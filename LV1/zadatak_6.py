'''
Napišite Python skriptu koja će učitati tekstualnu datoteku naziva SMSSpamCollection.txt [1]. 
Ova datoteka sadrži 425 SMS poruka pri čemu su neke označene kao spam, a neke kao ham. 

a) Izračunajte koliki je prosječan broj riječi u SMS porukama koje su tipa ham, a koliko je prosječan broj riječi u porukama koje su tipa spam.
b) Koliko SMS poruka koje su tipa spam završava uskličnikom ?
'''

naziv = input("Ime datoteke: ")

try:
    file = open(naziv)
except:
    print("Datoteka se ne može otvoriti.")
    quit()

ham = []
spam = []
usklicnik = 0

for line in file:
    line = line.rstrip()
    
    if "\t" in line:
        dijelovi = line.split("\t")
        tip = dijelovi[0]
        poruka = dijelovi[1]
        
        rijeci = len(poruka.split())
        
        if tip == "ham":
            ham.append(rijeci)
        elif tip == "spam":
            spam.append(rijeci)
            if poruka.endswith("!"):
                usklicnik += 1

file.close()

if len(ham) > 0:
    ham_avg = sum(ham) / len(ham)
    print("prosječan broj riječi u SMS porukama koje su tipa ham:", round(ham_avg, 2))

if len(spam) > 0:
    spam_avg = sum(spam) / len(spam)
    print("prosječan broj riječi u SMS porukama koje su tipa spam:", round(spam_avg, 2))

print("Broj SMS poruka koje su tipa spam i završavaju uskličnikom:", usklicnik)
