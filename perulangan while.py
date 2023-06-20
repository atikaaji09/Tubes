i = 0
while i <= 7:
    print("hello world!")
    i += 1

# perulangan increament
a = 1
b = 10
while a < b:
    print("step ke-", a)
    a += 1

# perulangan decrement
a = 10
b = 0 
while a > b:
    print("Kuota internet anda sisa", a , "GB")
    a-=1

# fungsi break 
a = 0
while True:
    print("Step ke-", a, "!")
    a += 1
    if a == 7:
        print("Step ke-", a, "dihentikan!")
        break

# fungsi continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)



