from .functions import*

def ubah_stok(x):
    global game

    id = input('Masukkan ID x: ')

    for i in range(length(x)):
        if id == x[i][0]:
            tambah = int(input('Masukkan jumlah: '))
            if tambah < 0 and abs(tambah) > x[i][5]:
                print('Stok x',x[i][1],'gagal dikurangi karena stok kurang. Stok sekarang: ',x[i][5], '(<',abs(tambah),')')
            else:
                x[i][5] = str(int(x[i][5]) + tambah)
                if tambah > 0:
                    print('Stok x', x[i][1],'berhasil ditambahkan. Stok sekarang: ',x[i][5])
                else:
                    print('Stok x', x[i][1],'berhasil dikurangi. Stok sekarang: ',x[i][5])
            break
    else:
        print('Tidak ada x dengan ID tersebut!')