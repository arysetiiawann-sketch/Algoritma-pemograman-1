# Menukar isi gelas A dan B
gelas_A = "Kopi"
gelas_B = "Teh"
gelas_C = ""

gelas_C = gelas_A
gelas_A = gelas_B
gelas_B = gelas_C
gelas_C = ""

print("Isi gelas A:", gelas_A)
print("Isi gelas B:", gelas_B)
print("Isi gelas C:", gelas_C)
print("Penukaran selesai.\n")

# Menghitung keliling dan luas persegi
while True:
    try:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        if sisi > 0:
            break
        print("Sisi harus lebih besar dari 0.")
    except ValueError:
        print("Masukkan angka yang benar.")

keliling = 4 * sisi
luas = sisi * sisi

print("\nMenghitung hasil...")
print("Wah, hasilnya sepertinya besar sekali!")
print("Tenang, cuma prank. Ini hasil yang sebenarnya:\n")

print("\nHasil perhitungan")
print("Panjang sisi:", sisi)
print("Keliling: 4 x", sisi, "=", keliling)
print("Luas:", sisi, "x", sisi, "=", luas)