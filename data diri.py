print("=============INPUT============")
nama = input("Nama: ")
jenis_kelamin = input("Jenis Kelamin (L/P): ")
agama = int(input("Agama: "))
#1=Islam, 2=Kristiani, 3=Budha, 4=Khatolik, 5=Hindu
if(agama==1):
    agama = "Islam"
elif(agama==2):
    agama = "Kristiani"
elif(agama==3):
    agama = "Budha"
elif(agama==4):
    agama = "Khatolik"
elif(agama==5):
    agama = "Hindu"
else:
    agama = "agama tidak ditemukan"

print("=========OUTPUT==========")
print("Nama: ", nama)
print("Jenis kelamin: ", jenis_kelamin)
print("Agama: ", agama)