from .functions import*

def list_game_toko(y):
    global game

    temp = []
    for i in range(length(y)):
        temp += [[y[i][0],y[i][1],y[i][2],y[i][3],y[i][4],y[i][5]]]
    # input skema sorting dan melakukan sorting
    skema = input("Skema sorting : ")
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
            print("invalid") 
            skema = input("Skema sorting : ")

    if atribut == 'harga':
        n = 4 # lokasi 'harga' di tabel 'game.csv' ada di kolom ke-4
    elif atribut == 'tahun':
        n = 3 # lokasi 'tahun' di tabel 'game.csv' ada di kolom ke-3
    elif atribut == 'id':
        n = 0 # lokasi 'tahun' di tabel 'game.csv' ada di kolom ke-0
    # selection sort

    if length(temp) > 1:
        for i in range(length(temp)):
            ekstrim = i # nilai ekstrim (min/maks)
            for j in range(length(temp)):
                if atribut == 'id':
                    temp                       
                else:
                    # selain atribut 'id', diurutinnya manual berdasarkan angka
                    if x == '-':
                        if (int(temp[ekstrim][n]) < int(temp[j][n])):
                            temp[i], temp[j] = temp[j], temp[i]
                    elif x == '+':
                        if (int(temp[ekstrim][n]) > int(temp[j][n])):
                            temp[i], temp[j] = temp[j], temp[i]

    for i in range(length(temp[0])):
        spaces(temp,i)
    num = [0 for i in range(length(temp))]
    for i in range(length(num)):
        num[i] = i+1
    numSpaces(num)
    for i in range(length(temp)):
        print(str(num[i]) + ' ' + temp[i][0] + ' | ' + temp[i][1] + ' | ' + temp[i][2] + ' | ' + temp[i][3] + ' | ' + temp[i][4] + ' | ' + temp[i][5])