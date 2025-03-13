class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_ID, *args, **kwargs):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_ID = nomor_ID
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang} (ID: {self.nomor_ID})"

class Mahasiswa(Orang):
    SARJANA = "Sarjana"
    MASTER = "Master"
    DOKTOR = "Doktor"
    
    def __init__(self, nama_depan, nama_belakang, nomor_ID, jenjang, *args, **kwargs):
        super().__init__(nama_depan, nama_belakang, nomor_ID, *args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []
    
    def enrol(self, *mata_kuliah):
        self.matkul.extend(mata_kuliah)
    
    def __str__(self):
        return super().__str__() + f" - Jenjang: {self.jenjang}, Matkul: {self.matkul}"

class Karyawan(Orang):
    TETAP = "Tetap"
    TDK_TETAP = "Tidak Tetap"
    
    def __init__(self, nama_depan, nama_belakang, nomor_ID, status_karyawan, *args, **kwargs):
        super().__init__(nama_depan, nama_belakang, nomor_ID, *args, **kwargs)
        self.status_karyawan = status_karyawan
    
    def __str__(self):
        return super().__str__() + f" - Status: {self.status_karyawan}"

class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_ID, status_karyawan, *args, **kwargs):
        super().__init__(nama_depan, nama_belakang, nomor_ID, status_karyawan, *args, **kwargs)
        self.matkul_diajar = []
    
    def mengajar(self, *mata_kuliah):
        self.matkul_diajar.extend(mata_kuliah)
    
    def __str__(self):
        return super().__str__() + f" - Matkul Diajar: {self.matkul_diajar}"

class Pelajar:
    def __init__(self, *args, **kwargs):
        self.matkul = []
        super().__init__(*args, **kwargs)
    
    def enrol(self, *mata_kuliah):
        self.matkul.extend(mata_kuliah)

class Pengajar:
    def __init__(self, *args, **kwargs):
        self.matkul_diajar = []
        super().__init__(*args, **kwargs)
    
    def mengajar(self, *mata_kuliah):
        self.matkul_diajar.extend(mata_kuliah)

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomor_ID, *args, **kwargs):
        super().__init__(nama_depan, nama_belakang, nomor_ID, *args, **kwargs)
    
    def __str__(self):
        return super().__str__() + f" - Matkul Diambil: {self.matkul}, Matkul Diajar: {self.matkul_diajar}"

uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data", "Pemrograman")
uswatun.mengajar("Kecerdasan Artifisial", "Jaringan Syaraf Tiruan")
print(uswatun)