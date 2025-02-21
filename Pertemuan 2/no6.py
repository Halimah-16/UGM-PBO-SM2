class Manusia:
    def __init__(self, nama, umur):  
        self.nama = nama
        self.umur = umur
    
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Umur: {self.umur} Tahun")

def main():
    nama_input = input("Masukkan nama: ")
    umur_input = int(input("Masukkan umur: "))  
    
    manusia1 = Manusia(nama_input, umur_input)
    manusia1.tampilkan_info()

if __name__ == '__main__':
    main()
    