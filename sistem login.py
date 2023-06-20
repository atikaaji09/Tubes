print("=======SISTEM LOGIN SEDERHANA========")
username = input("Masukkan username: ")
password = input("Masukkan password: ")

# Mengecek apakah username dan password sudah benar
if username == "atikaaji" and password == "12345":
    print("Selamat datang atikaaji!")
else:
    # Jika salah, iterasi sampai lebih dari tiga kali
    for i in range(3):
        password = input("Coba cek kembali, username atau password salah. ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if password == "12345":
            print("Login berhasil!")
            break
    else:
        print("Login gagal! Anda sudah mencoba login lebih dari tiga kali. Silahkan coba lagi nanti.")
        
    
