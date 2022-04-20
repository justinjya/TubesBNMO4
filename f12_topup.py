from .functions import*

# Fungsi topup menerima parameter yaitu variabel user
def topup(user):
    # Input username dan jumlah penambahan saldo
    username = input('Masukkan username: ')
    tambah = int(input('Masukkan saldo: '))

    # Looping untuk mencari indeks username yang terdaftar dalam data
    for i in range(length(user)):
        if username == user[i][1]:
            # Validasi bahwa saldo akhir tidak bisa kurang dari 0
            if tambah < 0 and abs(tambah) > user[i][5]:
                print('Masukan tidak valid')
            else:
                # Mengubah saldo
                user[i][5] = str(int(user[i][5]) + tambah)
                if tambah > 0:
                    print('Top up berhasil. Saldo', user[i][2], 'bertambah menjadi', user[i][5])
                else:
                    print('Pengurangan berhasil. Saldo', user[i][2], 'berkurang menjadi', user[i][5])
            break
    # Jika username tidak ditemukan
    else:
        print('Username', username, 'tidak ditemukan,')
