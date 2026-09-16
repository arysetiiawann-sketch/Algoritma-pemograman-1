# Menghitung keliling dan luas persegi
print("=" * 42)
print("       KALKULATOR PERSEGI SEDERHANA")
print("=" * 42)

while True:
	try:
		sisi = float(input("Masukkan panjang sisi persegi: "))
		if sisi <= 0:
			print("Sisi harus lebih besar dari 0. Coba lagi.")
			continue
		break
	except ValueError:
		print("Input harus berupa angka. Coba lagi.")

keliling = 4 * sisi
luas = sisi * sisi

print("\nHASIL PERHITUNGAN")
print(f"Panjang sisi : {sisi:g}")
print(f"Keliling     : 4 x {sisi:g} = {keliling:g}")
print(f"Luas         : {sisi:g} x {sisi:g} = {luas:g}")
print("Terima kasih sudah menggunakan program ini!")
