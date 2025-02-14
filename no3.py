niu = int(input("Masukkan NIU: "))
tugas = float(input("Masukkan nilai tugas: "))
laporan = float(input("Masukkan nilai laporan: "))

rata_rata = (tugas + laporan) / 2
if rata_rata < 40:
    print("Nilai akhir: K")
else:
    ujian = float(input("Masukkan nilai ujian: "))
    nilai_akhir = (0.25 * tugas) + (0.25 * laporan) + (0.50 * ujian)
    
    if nilai_akhir >= 80:
        print("Nilai akhir: A")
    elif nilai_akhir >= 70:
        print("Nilai akhir: B")
    elif nilai_akhir >= 60:
        print("Nilai akhir: C")
    elif nilai_akhir >= 50:
        print("Nilai akhir: D")
    else:
        print("Nilai akhir: E")
