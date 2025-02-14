import math

r = float(input("Masukkan jari-jari: "))
luas = math.pi * r * r
keliling = 2 * math.pi * r

print("Luas lingkaran: " + str(round(luas, 2)))
print("Keliling lingkaran: " + str(round(keliling, 2)))
