from .functions import*

# Fungsi list_game menerima parameter yaitu variabel game, kepemilikan, user_id
def list_game(game,kepemilikan,user_id):
    # Inisialisasi jumlah indeks, temporary array untuk menyimpan data 'game_id', dan temporary array untuk menyimpan game sesuai data 'game_id'
    count = 0
    temp = []
    tempo = []

    # Mengisi temporary array dengan data 'game_id'
    for i in range(length(kepemilikan)):
        if user_id == kepemilikan[i][1]: # Validasi user_id yang sesuai dengan data kemepilikan
            count += 1 # Menambah jumlah indeks sesuai data kepemilikan sesuai 'user_id' dengan 1
            temp += [kepemilikan[i][0]] # y[i][0] yaitu game_id
    
    # Mengisi temporary array dengan game sesuai data 'game_id'
    # game[i][0] yaitu game_id, game[i][1] yaitu nama, game[i][2] yaitu kategori, game[i][3] yaitu tahun rilis, game[i][4] yaitu harga
    for i in range(length(game)):
        for j in range(length(temp)):
            if temp[j] == game[i][0]:
                tempo += [[game[i][0],game[i][1],game[i][2],game[i][3],game[i][4]]]
    
    # Output daftar game yang dimiliki 'user_id'
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
            # tempo[i][0] yaitu game_id, tempo[i][1] yaitu nama, tempo[i][2], yaitu kategori, tempo[i][3] yaitu tahun rilis, tempo[i][4] yaitu harga
            print(str(num[i]) + ' ' + tempo[i][0] + ' | ' + tempo[i][1] + ' | ' + tempo[i][2] + ' | ' + tempo[i][3] + ' | ' + tempo[i][4])
