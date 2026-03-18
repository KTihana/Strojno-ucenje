'''
Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu. 
Koristite ugrađenu Python metodu input(). Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran. 
Na kraju prepravite rješenje na način da ukupni iznos izračunavate u zasebnoj funkciji naziva total_euro.

Primjer:
Radni sati: 35 h
eura/h: 8.5
Ukupno: 297.5 eura
'''


sati = float(input("Radni sati: "))
cijena = float(input("Euro/h: "))

ukupno = sati * cijena

print("Radni sati:", sati, "h")
print("eura/h:", cijena)
print("Ukupno:", ukupno, "eura")
