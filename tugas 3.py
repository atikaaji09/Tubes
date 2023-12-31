def bubble_sort(keyword, nomer):
    for i in range(len(nomer)):
        for j in range(len(nomer) - i - 1):
            if str(nomer[j]).lower() > str(nomer[j+1]).lower():
                nomer[j], nomer[j+1] = nomer[j+1], nomer[j]
    return binary_search(keyword, nomer)


def binary_search(keyword, data):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if str(data[mid]).lower() > keyword.lower():
            right = mid - 1
        elif str(data[mid]).lower() < keyword.lower():
            left = mid + 1
        else:
            print(data)
            print(f"Keyword {keyword} has been found at index {mid}")
            return mid

    print(f"Keyword {keyword} not found")
    return -1

data = [17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1]
keyword = input("Input keyword: ")
bubble_sort(keyword, data)