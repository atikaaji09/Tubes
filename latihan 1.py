# Tambah data mhs
def addMahasiswa():
    jumlah = int(input("Jumlah Mahasiswa :"))
    Mahasiswa = []
    while(jumlah > 0):
        nama = input("Nama Mahasiswa :")
        Mahasiswa.append(nama)
        jumlah = jumlah - 1

    while(True):
        panggil(Mahasiswa)
        jumlah = jumlah - 1
        if(jumlah<0):
            break

# hapus data mhs
def removeMahasiswa(arrayMahasiswa):
    Mahasiswa = arrayMahasiswa
    print("Data Mahasiswa %s" %arrayMahasiswa)
    Mahasiswa.remove(input("Hapus Mahasiswa :"))
    print("Data Mahasiswa %s" %Mahasiswa)
    panggil(Mahasiswa)

# urutkan data mhs
def ascMahasiswa(arrayMahasiswa):
    Mahasiswa = arrayMahasiswa
    Mahasiswa.sort()
    print(Mahasiswa)
    panggil(Mahasiswa)

# lihat data mhs
def viewMahasiswa(arrayMahasiswa):
    Mahasiswa = arrayMahasiswa
    for x in Mahasiswa:
        print("Nama Mahasiswa : %s" %x)
    panggil(arrayMahasiswa)

# menu
def panggil(arrayMahasiswa):
    print("\n<============= Menu Data Mahasiswa =============>")
    print("1. Tambah Data Mahasiswa")
    print("2. Hapus Data Mahasiswa")
    print("3. Urutkan Data Mahasiswa")
    print("4. Lihat Data Mahasiswa")
    print("5. Tutup")

    pilih = int(input("Pilih :"))
    if(pilih==1):
        addMahasiswa()
    elif(pilih==2):
        removeMahasiswa(arrayMahasiswa)
    elif(pilih==3):
        ascMahasiswa(arrayMahasiswa)
    elif(pilih==4):
        viewMahasiswa(arrayMahasiswa)
    else:
        print("Selesai")

addMahasiswa()

