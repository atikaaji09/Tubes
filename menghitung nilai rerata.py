array = []

rerata = int(input('\nMasukkan Jumlah Mata Kuliah : ')) 
print()

for i in range(rerata):
    nilai = float(input('Masukkan nilai mata kuliah ke-{} : '.format(i + 1)))
    array.append(nilai)
rata = sum(array)/rerata

print()
if rata < 100  and rata  >= 90 :
    print('Hasil Predikat A dengan nilai : ')
    for x in range(rerata):
        print('Mata kuliah ke-{}' .format(x), ' : ', (array[x]))
elif rata < 90 and rata >= 70 :
    print('Hasil Predikat B dengan nilai : ')
    for x in range(rerata):
        print('Mata kuliah ke-{}' .format(x), ' : ', (array[x]))
elif rata < 70 and rata >= 50 :
    print('Hasil Predikat C dengan nilai : ')
    for x in range(rerata):
        print('Mata kuliah ke-{}' .format(x), ' : ', (array[x]))
elif rata < 50 and rata >= 30 :
    print('Hasil Predikat D dengan nilai : ')
    for x in range(rerata):
        print('Mata kuliah ke-{}' .format(x), ' : ', (array[x]))
elif rata < 30 and rata >= 0 :
    print('Hasil Predikat E dengan nilai : ')
    for x in range(rerata):
        print('Mata kuliah ke-{}' .format(x), ' : ', (array[x]))
else:
    print('Nilai tidak valid !')