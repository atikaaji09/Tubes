huruf = input("Masukkan huruf: ")
if huruf.isalpha():
    if huruf.lower() in ['a', 'i', 'u', 'e', 'o']:
        print("Huruf vokal")
    else:
        print("Huruf konsonan")
else:
    print("Inputan bukan huruf")

