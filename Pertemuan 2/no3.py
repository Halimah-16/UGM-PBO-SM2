class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luas(self):
        return self.sisi * self.sisi
    
    def keliling(self):
        return 4 * self.sisi

persegi1 = Persegi(123)
print("Luas:", persegi1.luas())
print("Keliling:", persegi1.keliling())
