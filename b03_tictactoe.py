from .functions import*

papan = ['#','#','#','#','#','#','#','#','#']

def gambarKotak(papan):
    for i in range(3):
        print(papan[i], end = '')
    print('')
    for i in range(3):
        print(papan[i+3], end = '')
    print('')
    for i in range(3):
        print(papan[i+6], end = '')
    print('')

def tictactoe():
    gambarKotak(papan)
    count = 0
    simbol = ''
    
    while count != 9:
        if count % 2 == 0:
            simbol = 'X'
            print('Giliran X')
        else:
            simbol = 'O'
            print('Giliran O')
        # Horizontal
        if papan[0] == papan[1] == papan[2] == 'X' or papan[0] == papan[1] == papan[2] == 'O':
            print('Pemenangnya adalah', papan[0])
            break
        elif papan[3] == papan[4] == papan[5] == 'X' or papan[3] == papan[4] == papan[5] == 'O':
            print('Pemenangnya adalah', papan[3])
            break
        elif papan[6] == papan[7] == papan[8] == 'X' or papan[6] == papan[7] == papan[8] == 'O':
            print('Pemenangnya adalah', papan[6])
            break
        # Vertikal
        elif papan[0] == papan[3] == papan[6] == 'X' or papan[0] == papan[3] == papan[6] == 'O':
            print('Pemenangnya adalah', papan[0])
            break
        elif papan[1] == papan[4] == papan[7] == 'X' or papan[1] == papan[4] == papan[7] == 'O':
            print('Pemenangnya adalah', papan[1])
            break
        elif papan[2] == papan[5] == papan[8] == 'X' or papan[2] == papan[5] == papan[8] == 'O':
            print('Pemenangnya adalah', papan[2])
            break
        # Nyerong
        elif papan[0] == papan[4] == papan[8] == 'X' or papan[0] == papan[4] == papan[8] == 'O':
            print('Pemenangnya adalah', papan[0])
            break
        elif papan[6] == papan[4] == papan[2] == 'X' or papan[6] == papan[4] == papan[2] == 'O':
            print('Pemenangnya adalah', papan[6])
            break
        inpt = int(input('Masukkan nomor kotak: '))
        if inpt <= 9 and papan[inpt-1] == '#':
            count += 1
            papan[inpt-1] = simbol
            gambarKotak(papan)
        else:
            print('Masukan salah')
        if count == 9:
            print('Tidak ada pemenang!')
