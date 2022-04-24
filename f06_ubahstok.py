from .functions import*

# Fungsi ubah_stok menerima parameter yaitu varriabel game
def ubah_stok(game):
    # Input id game
    id = input('Masukkan ID Game: ')

    # Looping untuk mencari indeks game yang terdaftar
    for i in range(length(game)):
        if id == game[i][0]:
            # Input perubahan stok
            tambah = int(input('Masukkan jumlah: '))
            if tambah < 0 and abs(tambah) > int(game[i][5]): # Validasi bahwa hasil akhir stok tidak bisa kurang dari 0
                print('Stok game',game[i][1],'gagal dikurangi karena stok kurang. Stok sekarang:',game[i][5], '(<',abs(tambah),')')
            else:
                # Menambah stok
                game[i][5] = str(int(game[i][5]) + tambah)
                if tambah > 0:
                    print('Stok game', game[i][1],'berhasil ditambahkan. Stok sekarang:',game[i][5])
                else:
                    print('Stok game', game[i][1],'berhasil dikurangi. Stok sekarang:',game[i][5])
            break
    else: # Jika id game tidak terdaftar dalam data
        print('Tidak ada game dengan ID tersebut!')
