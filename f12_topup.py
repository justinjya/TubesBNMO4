from .functions import*

def topup(x):
    global user

    username = input('Masukkan username: ')
    tambah = int(input('Masukkan saldo: '))

    for i in range(length(x)):
        if username == x[i][1]:
            if tambah < 0 and abs(tambah) > x[i][5]:
                print('Masukan tidak valid')
            else:
                x[i][5] = str(int(x[i][5]) + tambah)
                if tambah > 0:
                    print('Top up berhasil. Saldo', x[i][2], 'bertambah menjadi', x[i][5])
                else:
                    print('Pengurangan berhasil. Saldo', x[i][2], 'berkurang menjadi', x[i][5])
            break
    else:
        print('Username', username, 'tidak ditemukan,')