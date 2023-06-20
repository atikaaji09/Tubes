# Method Prosedur
def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print("Hasil penjumlahan:", hasil)

def kurang(angka1, angka2):
    hasil = angka1 - angka2
    print("Hasil pengurangan:", hasil)

def kali(angka1, angka2):
    hasil = angka1 * angka2
    print("Hasil perkalian:", hasil)

def bagi(angka1, angka2):
    hasil = angka1 / angka2
    print("Hasil pembagian:", hasil)

def pangkat(angka1, angka2):
    hasil = angka1 ** angka2
    print("Hasil pangkat :", hasil)

def kalkulator():
    while True:
        print("======= Kalkulator Sederhana =======")
        print("Pilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Pangkat")

        pilihan = input("Masukkan pilihan : ")

        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))

        if pilihan == "1":
            tambah(angka1, angka2)
        elif pilihan == "2":
            kurang(angka1, angka2)
        elif pilihan == "3":
            kali(angka1, angka2)
        elif pilihan == "4":
            bagi(angka1, angka2)
        elif pilihan == "5":
            pangkat(angka1, angka2)
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

        lanjut = input("Apakah Anda ingin melanjutkan? (ya/tidak): ")
        if lanjut.lower() != "ya":
            break

# Panggil prosedur kalkulator untuk menjalankan program
kalkulator()


