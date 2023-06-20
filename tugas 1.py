def linear_search(keyword, plat):
    for i in range(len(plat)):
        if str(plat[i]).lower() == keyword.lower():
            print(f"Keyword {keyword} has found at indeks {i}")
            return i
    print(f"Keyword {keyword} not found")
    return -1
    
plat = ["R 2477 SR", "R 1234 DJ", "R 7015 LP", "R 0201 RR", "R 3304 DA",
            "R 2401 SK", "R 2103 RT", "R 1708 RI", "R 1111 SR", "R 4987 LH"]
keyword = input("Input Keyword :")
found = linear_search(keyword, plat)