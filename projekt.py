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
    ar=input("Add meg az eszköz árát:")
    db=input("Add meg az eszköz darabszámát:")
    eszkozok.append(Eszkoz(esz,ar,db))

print(len(eszkozok))
print(eszkozok[0].eszkoz)

