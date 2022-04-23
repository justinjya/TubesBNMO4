from .functions import*

# Fungsi search_my_game menerima parameter yaitu variabel game, kepemilikan, dan user_id
def search_my_game(game,kepemilikan,user_id):
    # Input id game dan tahun rilis
    id = input("Masukkan ID Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    
    # Inisialisasi kondisi awal found serta membuat temporary array
    found = False
    temp = []
    tempo  = []
    tempor = []

    # Mengisi temporary array 'temp' dengan data 'game_id' dalam kepemilikan
    for i in range(length(kepemilikan)):
        if user_id == kepemilikan[i][1]:
            temp += [kepemilikan[i][0]] # kepemilikan[i][0] yaitu game_id

    # Mengisi temporary array 'tempo' dengan data game sesuai 'game_id' dalam 'temp'
    # game[i][0] yaitu game_id, game[i][1] yaitu nama, game[i][2] yaitu kategori, game[i][3] yaitu tahun rilis, game[i][4] yaitu harga
    for i in range(length(game)):
        for j in range(length(temp)):
            if temp[j] == game[i][0]:
                    tempo += [[game[i][0],game[i][1],game[i][4],game[i][2],game[i][3]]]

    # Mengisi temporary array 'tempor' dengan data dalam 'temp' sesuai input id atau tahun rilis
    # tempo[i][0] yaitu game_id, tempo[i][1] yaitu nama, tempo[i][2], yaitu kategori, tempo[i][3] yaitu tahun rilis, tempo[i][4] yaitu harga
    for i in range(length(tempo)):
        if id == tempo[i][0]:
            found = True
            tempor += [[tempo[i][0],tempo[i][1],tempo[i][2],tempo[i][3],tempo[i][4]]]
        if tahun_rilis == tempo[i][4]:
            found = True
            tempor += [[tempo[i][0],tempo[i][1],tempo[i][2],tempo[i][3],tempo[i][4]]]
                
    print("Daftar game pada inventory yang memenuhi kriteria:")
    
    # Output daftar game yang dimiliki user sesuai kriteria
    if found == True:
        for i in range(length(tempor[0])):
            spaces(tempor,i)
        num = [0 for i in range(length(tempor))]
        for i in range(length(num)):
            num[i] = i+1
        numSpaces(num)
        for i in range(length(tempor)):
            # tempor[i][0] yaitu game_id, tempor[i][1] yaitu nama, tempor[i][2], yaitu kategori, tempor[i][3] yaitu tahun rilis, tempor[i][4] yaitu harga
            print(str(num[i]) + ' ' + tempor[i][0] + ' | ' + tempor[i][1] + ' | ' + tempor[i][2] + ' | ' + tempor[i][3] + ' | ' + tempor[i][4])
    else:
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria.') # Jika input id dan tahun rilis kosong
