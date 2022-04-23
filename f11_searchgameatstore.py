from .functions import*

# Fungsi search_game_at_store menerima parameter yaitu variabel game
def search_game_at_store(game):
    # Input id, nama, harga, kategori, dan tahun rilis
    id = input('Masukkan ID Game: ')
    nama = input('Masukkan Nama Game: ')
    harga = str(input('Masukkan Harga Game: '))
    kategori = str(input('Masukkan Kategori Game: '))
    tahun_rilis = str(input('Masukkan Tahun Rilis Game: '))
    
    # Inisialisasi temporary array dan kondisi awal found
    temp = []
    found = False

    print("Daftar game pada toko yang memenuhi kriteria:")

    # Mengisi temporary array dengan data dalam game sesuai input id, nama, harga, kategori, dan tahun rilis
    # game[i][0] yaitu game_id, game[i][1] yaitu nama, game[i][2] yaitu kategori, game[i][3] yaitu tahun rilis, game[i][4] yaitu harga, game[i][5] yaitu stok
    for i in range(length(game)):
        if id == game[i][0]:
            found = True
            temp += [[id,game[i][1],game[i][4],game[i][2],game[i][3],game[i][5]]]
        elif nama == game[i][1]:
            found = True
            temp += [[game[i][0],nama,game[i][4],game[i][2],game[i][3],game[i][5]]]
        elif harga == game[i][4]:
            found = True
            temp += [[game[i][0],game[i][1],harga,game[i][2],game[i][3],game[i][5]]]
        elif kategori == game[i][2]:
            found = True
            temp += [[game[i][0],game[i][1],game[i][4],kategori,game[i][3],game[i][5]]]
        elif tahun_rilis == game[i][3]:
            found = True
            temp += [[game[i][0],game[i][1],game[i][4],game[i][2],tahun_rilis,game[i][5]]]

    # Output daftar game pada toko sesuai kriteria
    if found == False:
        print('Tidak ada game yang memenuhi kriteria.')
    else:
        for i in range(length(temp[0])):
            spaces(temp,i)
        num = [0 for i in range(length(temp))]
        for i in range(length(num)):
            num[i] = i+1
        numSpaces(num)
        for i in range(length(temp)):
            # temp[i][0] yaitu game_id, temp[i][1] yaitu nama, temp[i][2], yaitu kategori, temp[i][3] yaitu tahun rilis, temp[i][4] yaitu harga, temp[i][5] yaitu stok
            print(str(num[i]) + ' ' + temp[i][0] + ' | ' + temp[i][1] + ' | ' + temp[i][2] + ' | ' + temp[i][3] + ' | ' + temp[i][4] + ' | ' + temp[i][5])
