from intervali import napraviIntervale
from procesi import *
from racunanjeInterval import izracunajIntervalRacunanja

def y(file):
    intervali = napraviIntervale(file) #pravi intervale od fajla
    procesi = napraviProcese(intervali) #sortira intervale po procesima
    pocetakRacunanja, krajRacunanja = izracunajIntervalRacunanja(procesi) #racuna period merenja

    for index in range(len(intervali)): #filtrira intervale koji nisu u periodu
        if(intervali[index].pocetak < pocetakRacunanja or intervali[index].kraj > krajRacunanja):
            for proces in procesi:
                if(proces.pid == intervali[index].pid):
                    proces.intervali.remove(intervali[index])

    suma = 0
    brojac1 = 0
    brojac2 = 0
    for proces in procesi:
        for i in range(1, len(intervali)):
            kasnjenje = intervali[i].pocetak - intervali[i - 1].pocetakSledeceg
            if(kasnjenje > 0):
                brojac1 += 1
                suma += kasnjenje
            else: brojac2 += 1
    
    n = brojac1 + brojac2
    prosecnoKasnjenje = suma / brojac1
    ukupnoKasnjenje = prosecnoKasnjenje * n
    
    return ukupnoKasnjenje / (krajRacunanja - pocetakRacunanja)
    


