from .functions import*

# Fungsi register menerima parameter yaitu variabel user
def register(user):
    # Input nama, username, dan password
    nama = input('Masukkan nama: ')
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')

    # Looping untuk validasi apakah username sudah dipakai atau belum
    for i in range(length(user)):
        if username == user[i][1]:
            print('Username', username, 'sudah terpakai, silahkan menggunakan username lain')
            break
    else:
        count = 0 # Inisialisasi panjang indeks username
        # Inisialisasi list untuk validasi karakter - karakter dalam username
        temp = temp = [ord(i) for i in username]
            
        # Looping untuk validasi apakah username sudah sesuai kriteria
        for i in range(length(username)):
            if length(username) < 5:
                print('Username harus memiliki minimal 5 karakter')
                break
            else:
                # Validasi apakah karakter - karakter dalam username sudah sesuai kriteria
                for i in range(length(username)):
                    if (temp[i] >= 97 and temp[i] <= 122) or (temp[i] >= 65 and temp[i] <= 90) or (temp[i] >= 48 and temp[i] <= 57) or (temp[i] == 45) or (temp[i] == 95):
                        count += 1 # Jika karakter dalam username sesuai dengan kriteria maka tambah jumlah username dengan 1
                if count == length(username):
                    print('Username', username, 'telah berhasil register ke dalam "Binomo".')
                    temp = [length(user)+1, username, nama, password, 'user', 0]
                    user += [temp]
                    break
                else:
                    print('Username hanya dapat mengandung huruf besar, huruf kecil, angka 0-9, underscore "_", dan strip "_"')
                    break
