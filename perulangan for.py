#for range max
for i in range(10):
    print("Hallo world!")

# # for range min, max
for i in range(1, 10):
    print(f"perulangan ke-{i}")
    # if i == 5:
    #     continue

# for range min, max, step
for i in range(0, 20, 2):
    print(f"step ke-{i}")

# for range min
for i in range(20, 0, -2):
    print(i)

# fungsi break 
for i in range(1, 10):
    print("Ini perulangan ke-", i)
    if i == 7:
        print("Perulangan ke-", i, "Dihentikan!")
        break

# fungsi continue 
for i in range(0, 10):
    if (i == 5):
        continue
    print(i)