from .functions import*

def buy_game(x,y,z,w,q):
    global user
    global game
    global kepemilikan
    global history
    global user_id

    id = input('Masukkan ID game: ')
    count = 0

    for i in range(length(z)):
        count += 1
        if id == z[i][0] and q == z[i][1]:
            print('Anda sudah memiliki game tersebut!')
            return
    if count == length(z):
        for i in range(length(y)):
            if id == y[i][0]:
                if int(y[i][5]) > 0:                
                    if int(x[int(q)-1][5]) >= int(y[i][4]):
                        temp = [y[i][0],q]
                        today = str(datetime.today().year)
                        tempo = [y[i][0],y[i][1],y[i][4],q,today]
                        x[int(q)-1][5] = str(int(x[int(q)-1][5]) - int(y[i][4]))
                        y[i][5] = str(int(y[i][5]) - 1)
                        z += [temp]
                        w += [tempo]
                        print('Game',y[i][1],'berhasil dibeli!')
                        break
                    else:
                        print('Saldo anda tidak cukup untuk membeli game tersebut!')
                        break
                else:
                    print('Stok game tersebut sedang habis!')
                    break