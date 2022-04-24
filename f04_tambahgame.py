from .functions import*

# Fungsi tambah_game menerima parameter yaitu variabel game
def tambah_game(game):
    # Input nama, kategori, tahun rilis, harga, dan stok game
    nama = input('Masukkan nama game: ')
    kategori = input('Masukkan kategori: ')
    tahun_rilis = input('Masukkan tahun rilis: ')
    harga = input('Masukkan harga: ')
    stok = input('Masukkan stok awal: ')

    # Melakukan pengulangan input nama, kategori, tahun rilis, harga, dan stok game jika inputan belum sesuai kriteria
    while nama == '' or kategori == '' or tahun_rilis == '' or harga == '' or stok == '':
        print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.')
        nama = input('Masukkan nama game: ')
        kategori = input('Masukkan kategori: ')
        tahun_rilis = input('Masukkan tahun rilis: ')
        harga = input('Masukkan harga: ')
        stok = input('Masukkan stok awal: ')
    else:
        # Menambah semua inputan kedalam data
        print('Selamat! Berhasil menambahkan game', nama)
        temp = ['G'+str(int(length(game))+1), nama, kategori, str(tahun_rilis), str(harga), str(stok)]
        game += [temp]
