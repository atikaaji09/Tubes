print("========PROGRAM SEDERHANA MENCARI KPK========")

bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))

# Mencari bilangan terbesar antara kedua bilangan yang dimasukkan
if bilangan1 > bilangan2:
    maksimum = bilangan1
else:
    maksimum = bilangan2

# Menentukan KPK
while(True):
    if maksimum % bilangan1 == 0 and maksimum % bilangan2 == 0:
        kpk = maksimum
        break
    maksimum += 1

# Menampilkan hasil
print("KPK dari", bilangan1, "dan", bilangan2, "adalah", kpk)
