from .functions import*

# Fungsi tambah_game menerima parameter x yaitu variabel game
def tambah_game(x):
    global game

    # Input nama, kategori, tahun rilis, harga, dan stok game
    nama = input('Masukkan nama game: ')
    kategori = input('Masukkan kategori: ')
    tahun_rilis = input('Masukkan tahun rilis: ')
    harga = input('Masukkan harga: ')
    stok = input('Masukkan stok awal: ')

    # Melakukan pengulangan input nama, kategori, tahun rilis, harga, dan stok game jika inputan belum sesuai kriteria
    while (nama != str and nama == '') and (kategori != str and kategori == '') and tahun_rilis != int and harga != int and stok != int:
        print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.')
        nama = input('Masukkan nama game: ')
        kategori = input('Masukkan kategori: ')
        tahun_rilis = input('Masukkan tahun rilis: ')
        harga = input('Masukkan harga: ')
        stok = input('Masukkan stok awal: ')
    else:
        # Menambah semua inputan kedalam data
        print('Selamat! Berhasil menambahkan game', nama)
        temp = ['G'+str(int(length(x))+1), nama, kategori, str(tahun_rilis), str(harga), str(stok)]
        x += [temp]
