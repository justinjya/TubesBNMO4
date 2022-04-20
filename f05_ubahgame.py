from .functions import*

# Fungsi ubah_game menerima parameter yaitu varibel game
def ubah_game(game):
    # Input id, nama, kategori, tahun rilis, harga
    id = input('Masukkan ID game: ')
    nama = input('Masukkan nama game: ')
    kategori = input('Masukkan kategori: ')
    tahun_rilis = input('Masukkan tahun rilis: ')
    harga = input('Masukkan harga: ')

    # Looping untuk mencari id apakah terdaftar dalam data
    for i in range(length(game)):
        if id == game[i][0]:
            # Jika id terdaftar, maka merubah data sesuai input
            if nama != '':
                game[i][1] = nama
            if kategori != '':
                game[i][2] = kategori
            if tahun_rilis != '':
                game[i][3] = str(tahun_rilis)
            if harga != '':
                game[i][4] = str(harga)
