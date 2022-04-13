from math import *
class Eszkoz:
    def __init__(self,e,a,d):
        self.eszkoz=e
        self.ar=int(a)
        self.db=int(d)
        self.koltseg=ar*db

eszkozszam=int(input("Kérlek add meg az eszközök számát!"))
eszkozok=[]
for i in range(eszkozszam):
    esz=input("Add meg az eszköz nevét:")
    ar=int(input("Add meg az eszköz árát:"))
    db=int(input("Add meg az eszköz darabszámát:"))
    eszkozok.append(Eszkoz(esz,ar,db))

print(len(eszkozok))
print(eszkozok[0].eszkoz)

class Eszkoz2:
    def __init__(self,eszk,ar,db):
        self.eszkoz=eszk
        self.ar=int(ar)
        self.db=int(db)
        self.koltseg=ar*db

eszkozszam2=int(input("Kérlek add meg az eszközök számát!"))
eszkozok2=[]
for i in range(eszkozszam2):
    eszk=input("Add meg az eszköz nevét:")
    ar=int(input("Add meg az eszköz árát:"))
    db=int(input("Add meg az eszköz darabszámát:"))
    eszkozok2.append(Eszkoz2(eszk,ar,db))

print(len(eszkozok2))
print(eszkozok2[0].eszkoz)

class Eszkoz3:
    def __init__(self,eszko,ara,dbja):
        self.eszkoz=eszko
        self.ar=int(ara)
        self.db=int(dbja)
        self.koltseg=ar*db

eszkozszam3=int(input("Kérlek add meg az eszközök számát!"))
eszkozok3=[]
for i in range(eszkozszam3):
    eszko=input("Add meg az eszköz nevét:")
    ara=int(input("Add meg az eszköz árát:"))
    dbja=int(input("Add meg az eszköz darabszámát:"))
    eszkozok3.append(Eszkoz2(eszko,arja,dbja))

print(len(eszkozok3))
print(eszkozok3[0].eszkoz)


