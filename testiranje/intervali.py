import matplotlib.pyplot as plt

class Interval:
    def __init__(self, pid, pocetak, kraj, pocetakSledeceg):
        self.pid = int(pid)
        self.pocetak = int(pocetak)
        self.kraj = int(kraj)
        self.pocetakSledeceg = int(pocetakSledeceg)
    
    def __str__(self):
        return (str(self.pid) + " " + str(self.pocetak) + "-" + str(self.kraj) + ", " + str(self.pocetakSledeceg))



def napraviIntervale(fajl):
    f = open(fajl, "r")
    lines = f.readlines()

    pocetak = []
    kraj = []

    pids = {}

    for line in lines:
        line = line.split()
        if(line[1] == "UZEO:"): 
            line.pop(1)
            pocetak.append(line)
        else:
            line.pop(1)
            kraj.append(line)

    intervali = []
    for i in range(len(lines) // 2):
        interval = Interval(
            pocetak[i][0], #pid
            pocetak[i][1], #pocetak intervala
            kraj[i][1],     #kraj intervala
            kraj[i][2]      #pocetak sledeceg intervala 
        )

        intervali.append(interval)
    
    return intervali
