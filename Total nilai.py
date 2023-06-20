print("====PROGRAM SEDERHANA MENGHITUNG JUMLAH TOTAL BILANGAN====")

bilangan = int(input("Masukkan bilangan: "))

# Inisialisasi variabel total dan string untuk menyimpan operasi matematika
total = 0
operasi = ""

# Menghitung total nilai dari bilangan 
for i in range(bilangan, 0, -1):
    total += i
    operasi += str(i)
    if i != 1:
        operasi += " + "

# hasil
print("Total nilai =", operasi, "=", total)










