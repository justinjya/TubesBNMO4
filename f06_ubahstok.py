from .functions import*

# Fungsi ubah_stok menerima parameter x yaitu varriabel game
def ubah_stok(x):
    global game

    # Input id game
    id = input('Masukkan ID Game: ')

    # Looping untuk mencari indeks game yang terdaftar
    for i in range(length(x)):
        if id == x[i][0]:
            # Input perubahan stok
            tambah = int(input('Masukkan jumlah: '))
            if tambah < 0 and abs(tambah) > x[i][5]: # Validasi bahwa hasil akhir stok tidak bisa kurang dari 0
                print('Stok x',x[i][1],'gagal dikurangi karena stok kurang. Stok sekarang: ',x[i][5], '(<',abs(tambah),')')
            else:
                # Menambah stok
                stok = int(x[i][5]) + tambah
                x[i][5] = str(stok)
                if tambah > 0:
                    print('Stok x', x[i][1],'berhasil ditambahkan. Stok sekarang: ',x[i][5])
                else:
                    print('Stok x', x[i][1],'berhasil dikurangi. Stok sekarang: ',x[i][5])
            break
    else: # Jika id game tidak terdaftar dalam data
        print('Tidak ada game dengan ID tersebut!')
