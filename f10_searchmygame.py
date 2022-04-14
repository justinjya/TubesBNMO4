from .functions import*

def search_my_game(x,y,z):
    global game
    global kepemilikan
    global user_id

    id = input("Masukkan ID Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    found = False
    temp = []
    tempo  = []
    tempor = []

    print("Daftar game pada inventory yang memenuhi kriteria:")

    for i in range(length(y)):
        if z == y[i][1]:
            temp += [y[i][0]]

    for i in range(length(x)):
        for j in range(length(temp)):
            if temp[j] == x[i][0]:
                    tempo += [[x[i][0],x[i][1],x[i][4],x[i][2],x[i][3]]]

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

    if found == True:
        for i in range(length(tempor[0])):
            spaces(tempor,i)
        num = [0 for i in range(length(tempor))]
        for i in range(length(num)):
            num[i] = i+1
        numSpaces(num)
        for i in range(length(tempor)):
            print(str(num[i]) + ' ' + tempor[i][0] + ' | ' + tempor[i][1] + ' | ' + tempor[i][2] + ' | ' + tempor[i][3] + ' | ' + tempor[i][4])
    else:
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria.')