from .functions import*

def search_game_at_store(x):
    global game

    id = input('Masukkan ID Game: ')
    nama = input('Masukkan Nama Game: ')
    harga = str(input('Masukkan Harga Game: '))
    kategori = str(input('Masukkan Kategori Game: '))
    tahun_rilis = str(input('Masukkan Tahun Rilis Game: '))
    temp = []
    found = False

    print("Daftar game pada toko yang memenuhi kriteria:")

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
