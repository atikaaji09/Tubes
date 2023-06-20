def nilai(nilai1, nilai2):
    if(nilai1>nilai2):
        print(nilai1)
    elif(nilai1==nilai2):
        print("tidak ada bilangan yang lebih besar")
    else:
        print(nilai2)

bilangan1 = int(input("Masukkan bilangan 1 :"))
bilangan2 = int(input("Masukkan bilangan 2 :"))
print("Bilangan yang paling besar adalah :")
nilai(bilangan1, bilangan2)