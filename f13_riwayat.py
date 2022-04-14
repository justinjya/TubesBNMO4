from .functions import*

def riwayat(x,y):
    global history
    global user_id

    temp = []
    for i in range(length(x)):
        temp += [[x[i][0],x[i][1],x[i][2],x[i][3],x[i][4]]]

    if length(x) == 0:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah "buy_game" untuk membeli.')
    else:
        for i in range(length(x[0])):
            spaces(temp,i)
        num = [0 for i in range(length(temp))]
        for i in range(length(num)):
            num[i] = i+1
        numSpaces(num)
        print('Daftar game:')
        for i in range(length(temp)):
            if y == temp[i][3]:
                print(str(num[i]) + ' ' + temp[i][0] + ' | ' + temp[i][1] + ' | ' + temp[i][2] + ' | ' + temp[i][4])