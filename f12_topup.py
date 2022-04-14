from .functions import*

# Fungsi topup menerima parameter x yaitu variabel user
def topup(x):
    global user

    # Input username dan jumlah penambahan saldo
    username = input('Masukkan username: ')
    tambah = int(input('Masukkan saldo: '))

    # Looping untuk mencari indeks username yang terdaftar dalam data
    for i in range(length(x)):
        if username == x[i][1]:
            # Validasi bahwa saldo akhir tidak bisa kurang dari 0
            if tambah < 0 and abs(tambah) > x[i][5]:
                print('Masukan tidak valid')
            else:
                # Mengubah saldo
                x[i][5] = str(int(x[i][5]) + tambah)
                if tambah > 0:
                    print('Top up berhasil. Saldo', x[i][2], 'bertambah menjadi', x[i][5])
                else:
                    print('Pengurangan berhasil. Saldo', x[i][2], 'berkurang menjadi', x[i][5])
            break
    # Jika username tidak ditemukan
    else:
        print('Username', username, 'tidak ditemukan,')
