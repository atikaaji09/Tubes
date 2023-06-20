print("<-----Menu Hitung Biaya Operasi----->")
def calculate_cost(operation, disease):
    cost = 0
    if operation == "Operasi Mata":
        if disease == "Katarak":
            cost = 7500000
        elif disease == "Plus / Minus":
            cost = 5000000
        elif disease == "Silinder":
            cost = 4000000
    elif operation == "Operasi Jantung":
        if disease == "Jantung Koroner":
            cost = 500000000
        elif disease == "Katup Jantung":
            cost = 350000000
        elif disease == "Otot Jantung":
            cost = 450000000
    return cost


print("1. Hitung Biaya Operasi Mata")
print("2. Hitung Biaya Operasi Jantung")

operation_choice = int(input("Masukkan pilihan: "))

if operation_choice == 1:
    print("Jenis Penyakit Mata :")
    print("1. Katarak")
    print("2. Plus / Minus")
    print("3. Silinder")
    disease_choice = int(input("Masukkan Jenis Penyakit Mata : "))
    if disease_choice == 1:
        print("Biaya operasi Katarak adalah Rp. 7.500.000")
    elif disease_choice == 2:
        print("Biaya operasi Plus / Minus adalah Rp. 5.000.000")
    elif disease_choice == 3:
        print("Biaya operasi Silinder adalah Rp. 4.000.000")
    else:
        print("Pilihan tidak valid")
elif operation_choice == 2:
    print("Jenis Penyakit Jantung:")
    print("1. Jantung Koroner")
    print("2. Katup Jantung")
    print("3. Otot Jantung")
    disease_choice = int(input("Masukkan Jenis Penyakit Jantung : "))
    if disease_choice == 1:
        print("Biaya operasi Jantung Koroner adalah Rp. 500.000.000")
    elif disease_choice == 2:
        print("Biaya operasi Katup Jantung adalah Rp. 350.000.000")
    elif disease_choice == 3:
        print("Biaya operasi Otot Jantung adalah Rp. 450.000.000")
    else:
        print("Pilihan tidak valid")
else:
    print("Pilihan tidak valid")
