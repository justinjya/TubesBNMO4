from .functions import*

def list_game(x,y,z):
    global game
    global kepemilikan
    global user_id

    count = 0
    temp = []
    tempo = []

    for i in range(length(y)):
        if z == y[i][1]:
            count += 1
            temp += [y[i][0]]
    
    for i in range(length(x)):
        for j in range(length(temp)):
            if temp[j] == x[i][0]:
                tempo += [[x[i][0],x[i][1],x[i][2],x[i][3],x[i][4]]]
    
    print(tempo)
    
    print('Daftar game:')
    if count == 0:
        print('Maaf, kamu belum memiliki game. Ketik perintah "buy_game" untuk beli.')
    else:
        for i in range(length(tempo[0])):
            spaces(tempo,i)
        num = [0 for i in range(length(tempo))]
        for i in range(length(num)):
            num[i] = i+1
        numSpaces(num)
        for i in range(length(tempo)):
            print(str(num[i]) + ' ' + tempo[i][0] + ' | ' + tempo[i][1] + ' | ' + tempo[i][2] + ' | ' + tempo[i][3] + ' | ' + tempo[i][4])
