input_buku = []
def addbuku():
    jumlah = int(input("\nMasukkan Jumlah Buku : "))
    for i in range(jumlah):
        judul_buku = input(f"Masukkan Judul Buku Ke-{i + 1} :")
        input_buku.append(judul_buku)
        jumlah = jumlah - 1

        while (True):
            jumlah = jumlah - 1
            if(jumlah<0):
                break

def asc(arraybuku):
    for i in range(1, len(arraybuku)):
        item = arraybuku[i]
        j = i - 1
        
        while j >= 0 and arraybuku[j] > item:
            arraybuku[j + 1] = arraybuku[j]
            j -= 1

        arraybuku[j + 1] = item

    print("\n Sorting Buku Secara Ascending")
    print(" ")
    for x in range(len(arraybuku)):
        print(f"Judul Buku ke-{x + 1} : %s" %arraybuku[x])
    print(" ")

    return arraybuku

def desc(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] < item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item
        
    print("\n Sorting Buku Secara Descending")
    print(" ")
    for x in range(len(array)):
        print(f"Judul Buku Ke-{x + 1} : %s" %array[x])
    print(" ")

    return array


addbuku()
print("\n <============= Urutkan ? ==============>")
print("1. Ascending")
print("2. Descending")

pilih = int(input("Pilih :"))
if (pilih == 1):
    asc(input_buku)
elif (pilih == 2):
    desc(input_buku)
else:
    print("\n Pilihan Jenis Sorting Tidak Valid")