from y import y
import os
import matplotlib.pyplot as plt

class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y




path = "testovi"
testovi = os.listdir(path)

resenja = []
for test in testovi:
    res = y(path+"/"+test)
    resenja.append(Test(
        int(test),
        res
    ))

resenja = sorted(resenja, key=lambda instanca: instanca.x)

brojevi = []
rezultati = []
for resenje in resenja:
    brojevi.append(resenje.x)
    rezultati.append(resenje.y)
    
plt.plot(brojevi, rezultati)
plt.show()


