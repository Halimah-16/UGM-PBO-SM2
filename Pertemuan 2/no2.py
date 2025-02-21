class Transportasi:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    
    def info(self):
        print("Transportasi : " + self.jenis )
        print("Merk : " + self.merk)
        print("Warna : " + self.warna)

# Membuat objek dari kelas Transportasi
Transportasi1 = Transportasi("Motor", "Honda", "Putih")
Transportasi1.info()
