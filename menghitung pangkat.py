print("=======PROGRAM SEDERHANA MENGHITUNG PANGKAT========")

bilangan = int(input("Masukkan bilangan : "))
pencacah = int(input("Masukkan pencacah : "))
hasil_pangkat = 1
i = 1
while i <= pencacah:
    hasil_pangkat *= bilangan
    i += 1
print("Hasil pangkat = ", hasil_pangkat)
