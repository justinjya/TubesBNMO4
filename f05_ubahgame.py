from .functions import*

def ubah_game(x):
    global game

    # Input id, nama, kategori, tahun rilis, harga
    id = input('Masukkan ID game: ')
    nama = input('Masukkan nama game: ')
    kategori = input('Masukkan kategori: ')
    tahun_rilis = input('Masukkan tahun rilis: ')
    harga = input('Masukkan harga: ')

    # Looping untuk mencari id apakah terdaftar dalam data
    for i in range(length(x)):
        if id == x[i][0]:
            # Jika id terdaftar, maka merubah data sesuai input
            if nama != '':
                x[i][1] = nama
            if kategori != '':
                x[i][2] = kategori
            if tahun_rilis != '':
                x[i][3] = str(tahun_rilis)
            if harga != '':
                x[i][4] = str(harga)
