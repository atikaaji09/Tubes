# selection sorting
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j] :
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

nama = ['Zhafira', 'Nirmala', 'Aksara', 'Nalendra', 'Cakra', 'Sastra', 'Agni', 'Bagas', 'Jerome', 'Kiara']
print("Nama 10 Anggota Organisasi")
print(f"Before : {nama}")
selection_sort(nama)
print(f"After : {nama}")

