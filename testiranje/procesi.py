class Proces:
    def __init__(self, pid, intervali):
        self.pid = pid
        self.intervali = intervali
        self.pocetak = intervali[0].pocetak
        
    def updatePocetak(self):
        self.pocetak = self.intervali[0].pocetak

    def updateKraj(self):
        self.kraj = self.intervali[-1].kraj


    def __str__(self):
        return str(self.pid) + " " + str(self.pocetak) + "-" + str(self.kraj)
        

def postoji(procesi, interval):
    for i in range(len(procesi)):
        if(interval.pid == procesi[i].pid): return i
    return -1

def napraviProcese(intervali):
    procesi = []
    for interval in intervali:
        index = postoji(procesi, interval)
        if(index == -1):
            procesi.append(Proces(
                interval.pid,
                [interval]
            ))
        else:
            procesi[index].intervali.append(interval)

    for proces in procesi: proces.updateKraj()

    return procesi

    

