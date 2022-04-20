from .functions import*

# Fungsi list_game_toko menerima parameter yaitu variabel game
def list_game_toko(game):
    # Inisialisasi temporary array kosong untuk meng-copy list data game
    temp = []
    # Mengisi temporary array dengan list data game
    # y[i][0] yaitu game_id, game[i][1] yaitu nama, game[i][2] yaitu kategori, game[i][3] yaitu tahun rilis, game[i][4] yaitu harga, game[i][5] yaitu stok
    for i in range(length(game)):
        temp += [[game[i][0],game[i][1],game[i][2],game[i][3],game[i][4],game[i][5]]]
        
    # Input skema sorting dan melakukan sorting
    skema = input('Skema sorting : ')
    
    # sorted_list = sortedlist(skema)
    valid = False

    while not valid:
        if skema == '':
            atribut = 'id'
            x = '+'
            valid = True
        elif skema == 'tahun+':
            atribut = 'tahun' 
            x = '+'
            valid = True
        elif skema == 'tahun-':
            atribut = 'tahun' 
            x = '-'
            valid = True
        elif skema == 'harga+':
            atribut = 'harga' 
            x = '+'
            valid = True
        elif skema == 'harga-':
            atribut = 'harga' 
            x = '-'
            valid = True
        else:
            print('Skema sorting tidak valid!') 
            skema = input("Skema sorting : ")

    if atribut == 'harga':
        n = 4 # Lokasi 'harga' di tabel 'game.csv' ada di kolom ke-4
    elif atribut == 'tahun':
        n = 3 # Lokasi 'tahun' di tabel 'game.csv' ada di kolom ke-3
    elif atribut == 'id':
        n = 0 # Lokasi 'tahun' di tabel 'game.csv' ada di kolom ke-0
        
    # Selection sort
    if length(temp) > 1:
        for i in range(length(temp)):
            ekstrim = i # Nilai ekstrim (min/maks)
            for j in range(length(temp)):
                if atribut == 'id': # Sorting berdasarkan 'id' ( Tidak perlu melakukan sorting karena id selalu dalam keadaan sorted ascending )
                    temp                       
                else:
                    # Selain atribut 'id', diurutinnya manual berdasarkan angka
                    if x == '-':
                        if (int(temp[ekstrim][n]) > int(temp[j][n])):
                            temp[i], temp[j] = temp[j], temp[i]
                    elif x == '+':
                        if (int(temp[ekstrim][n]) < int(temp[j][n])):
                            temp[i], temp[j] = temp[j], temp[i]
                            
    # Output list yang sudah diurutkan sesuai atribut
    for i in range(length(temp[0])):
        spaces(temp,i)
    num = [0 for i in range(length(temp))]
    for i in range(length(num)):
        num[i] = i+1
    numSpaces(num)
    for i in range(length(temp)):
        # temp[i][0] yaitu game_id, temp[i][1] yaitu nama, temp[i][2], yaitu kategori, temp[i][3] yaitu tahun rilis, temp[i][4] yaitu harga, temp[i][5] yaitu stok
        print(str(num[i]) + ' ' + temp[i][0] + ' | ' + temp[i][1] + ' | ' + temp[i][2] + ' | ' + temp[i][3] + ' | ' + temp[i][4] + ' | ' + temp[i][5])
