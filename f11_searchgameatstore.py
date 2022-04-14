from .functions import*

# Fungsi search_game_at_store menerima parameter x yaitu variabel game
def search_game_at_store(x):
    global game

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
    # x[i][0] yaitu game_id, x[i][1] yaitu nama, x[i][2], yaitu kategori, x[i][3] yaitu tahun rilis, x[i][4] yaitu harga, x[i][5] yaitu stok
    for i in range(length(x)):
        if id == '' or nama == '' or harga == '' or kategori == '' or tahun_rilis == '':
            if id == x[i][0]:
                found = True
                temp += [[id,x[i][1],x[i][4],x[i][2],x[i][3],x[i][5]]]
            elif nama == x[i][1]:
                found = True
                temp += [[x[i][0],nama,x[i][4],x[i][2],x[i][3],x[i][5]]]
            elif harga == x[i][4]:
                found = True
                temp += [[x[i][0],x[i][1],harga,x[i][2],x[i][3],x[i][5]]]
            elif kategori == x[i][2]:
                found = True
                temp += [[x[i][0],x[i][1],x[i][4],kategori,x[i][3],x[i][5]]]
            elif tahun_rilis == x[i][3]:
                found = True
                temp += [[x[i][0],x[i][1],x[i][4],x[i][2],tahun_rilis,x[i][5]]]

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
            print(str(num[i]) + ' ' + temp[i][0] + ' | ' + temp[i][1] + ' | ' + temp[i][2] + ' | ' + temp[i][3] + ' | ' + temp[i][4] + ' | ' + temp[i][5])
