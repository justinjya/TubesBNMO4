from .functions import*

def ubah_game(x):
    global game

    id = input('Masukkan ID game: ')
    nama = input('Masukkan nama game: ')
    kategori = input('Masukkan kategori: ')
    tahun_rilis = input('Masukkan tahun rilis: ')
    harga = input('Masukkan harga: ')

    for i in range(length(x)):
        if id == x[i][0]:
            if nama != '':
                x[i][1] = nama
            if kategori != '':
                x[i][2] = kategori
            if tahun_rilis != '':
                x[i][3] = str(tahun_rilis)
            if harga != '':
                x[i][4] = str(harga)