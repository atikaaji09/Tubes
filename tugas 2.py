def bubble_sort(keyword, nim):
    for i in range(len(nim)):
        for j in range(len(nim) - i - 1):
            if str(nim[j]).lower() > str(nim[j+1]).lower():
                nim[j], nim[j+1] = nim[j+1], nim[j]
    return binary_search(keyword, nim)

def binary_search(keyword, nim):
    left = 0
    right = len(nim) - 1

    while left <= right:
        mid = (left + right) // 2
        if str(nim[mid]).lower() > keyword.lower():
            right = mid - 1
        elif str(nim[mid]).lower() < keyword.lower():
            left = mid + 1
        else:
            print(nim)
            print(f"Keyword {keyword} has been found at index {mid}")
            return mid

    print(f"Keyword {keyword} not found")
    return -1

nim = [20103023, 20103002, 20103019, 20103001, 20103017, 20103005, 20103011, 20103003, 20103009, 20103021, 20103006, 
       20103015, 20103013, 20103007]
keyword = input("Input keyword: ")
bubble_sort(keyword, nim)
