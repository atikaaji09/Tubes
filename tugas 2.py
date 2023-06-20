# Method function
def hitung_luas(jari_jari):
    luas = 3.14 * jari_jari**2
    return luas

def hitung_keliling(jari_jari):
    keliling = 2 * 3.14 * jari_jari
    return keliling

# Membaca input dari pengguna
jari_jari = int(input("Masukkan jari-jari lingkaran : "))

# Menghitung dan mencetak luas lingkaran
luas = hitung_luas(jari_jari)
print("Luas lingkaran adalah :", luas)

# Menghitung dan mencetak keliling lingkaran
keliling = hitung_keliling(jari_jari)
print("Keliling lingkaran adalah :", keliling)


# Method prosedur
def hitung_luas(jari_jari):
    luas = 3.14 * jari_jari**2
    print("Luas lingkaran adalah :", luas)

def hitung_keliling(jari_jari):
    keliling = 2 * 3.14 * jari_jari
    print("Keliling lingkaran adalah :", keliling)

# Membaca input dari pengguna
jari_jari = int(input("Masukkan jari-jari lingkaran : "))

# Memanggil prosedur untuk menghitung luas lingkaran
hitung_luas(jari_jari)

# Memanggil prosedur untuk menghitung keliling lingkaran
hitung_keliling(jari_jari)
