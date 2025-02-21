class Mahasiswa:
    def __init__(self, nama, nim, angkatan, kelas):  # Konstruktor
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        self.kelas = kelas
    
    def tampilkan_info(self):  # Metode biasa
        print("Nama:", self.nama)
        print("NIM: ", self.nim)
        print("Angkatan: ", self.angkatan)
        print("Kelas: ", self.kelas)

mhs1 = Mahasiswa("Halimah", "24822", "2023", "A2")
mhs2 = Mahasiswa("Syania", "25098", "2024", "B2")

mhs1.tampilkan_info()
mhs2.tampilkan_info()
