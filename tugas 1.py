# Method Function
def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

bilangan = int(input("Masukkan bilangan : "))

# Pemanggilan method function
hasil = cek_ganjil_genap(bilangan)
print("Bilangan yang anda masukkan adalah", hasil)


# Method Prosedur
def tampilkan_ganjil_genap(nilai):
    if nilai % 2 == 0:
        print(f"Bilangan yang anda masukkan adalah Genap")
    else:
        print(f"Bilangan yang anda masukkan adalah Ganjil")

# Contoh Pemanggilan
bilangan = int(input("Masukkan bilangan: "))

# Pemanggilan method prosedur 
tampilkan_ganjil_genap(bilangan)



    
