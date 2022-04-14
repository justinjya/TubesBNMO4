from .functions import*

# Fungsi search_my_game menerima parameter x, y, dan z yaitu variabel game, kepemilikan, dan user_id
def search_my_game(x,y,z):
    global game
    global kepemilikan
    global user_id

    # Input id game dan tahun rilis
    id = input("Masukkan ID Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    
    # Inisialisasi kondisi awal found serta membuat temporary array
    found = False
    temp = []
    tempo  = []
    tempor = []

    # Mengisi temporary array 'temp' dengan data 'game_id' dalam kepemilikan
    for i in range(length(y)):
        if z == y[i][1]:
            temp += [y[i][0]] # y[i][0] yaitu game_id

    # Mengisi temporary array 'tempo' dengan data game sesuai 'game_id' dalam 'temp'
    # x[i][0] yaitu game_id, x[i][1] yaitu nama, x[i][2], yaitu kategori, x[i][3] yaitu tahun rilis, x[i][4] yaitu harga
    for i in range(length(x)):
        for j in range(length(temp)):
            if temp[j] == x[i][0]:
                    tempo += [[x[i][0],x[i][1],x[i][4],x[i][2],x[i][3]]]

    # Mengisi temporary array 'tempor' dengan data dalam 'temp' sesuai input id atau tahun rilis
    # tempo[i][0] yaitu game_id, tempo[i][1] yaitu nama, tempo[i][2], yaitu kategori, tempo[i][3] yaitu tahun rilis, tempo[i][4] yaitu harga
    if id != '':
        for i in range(length(tempo)):
            if id == tempo[i][0]:
                tempor += [[tempo[i][0],tempo[i][1],tempo[i][2],tempo[i][3],tempo[i][4]]]
                found = True
    if tahun_rilis != '':
        for i in range(length(tempo)):
            if tahun_rilis == tempo[i][4]:
                tempor += [[tempo[i][0],tempo[i][1],tempo[i][2],tempo[i][3],tempo[i][4]]]
                found = True
                
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
