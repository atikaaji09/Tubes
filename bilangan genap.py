
# print("=======MENCARI BILANGAN GENAP=======")
# bil = int(input("Masukkan bilangan maksimal: "))
# i = 0
# while i < bil:
#     print(i)
#     i+=6
#     if i == bil:
#         break

bilangan = int(input("Masukkan bilangan bulat positif (1-100): "))

if bilangan >= 1 and bilangan <= 100:
    if bilangan % 6 == 0:
        print(f"{bilangan} adalah kelipatan 6.")
    else:
        print(f"{bilangan} bukan kelipatan 6.")
else:
    print("Bilangan yang dimasukkan harus antara 1 hingga 100.")
