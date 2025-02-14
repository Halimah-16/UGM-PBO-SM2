num = int(input("Masukkan angka: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Bukan angka prima")
            break
    else:
        print("Angka prima")
else:
    print("Bukan angka prima")
