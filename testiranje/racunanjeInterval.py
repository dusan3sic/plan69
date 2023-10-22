def izracunajIntervalRacunanja(procesi):
    p = []
    k = []
    for proces in procesi:
        p.append(proces.pocetak)
        k.append(proces.kraj)
    
    return (max(p), min(k))