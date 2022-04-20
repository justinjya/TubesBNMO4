from .functions import*

# Fungsi buy_game menerima parameter yaitu varibael user, game, kepemilikan, history, user_id
def buy_game(user,game,kepemilikan,history,user_id):
    # Input id game
    id = input('Masukkan ID game: ')
    # Inisialisasi jumlah game yang ada di data kepemilikan
    count = 0

    # Looping untuk validasi apakah user_id sudah memiliki id game
    for i in range(length(kepemilikan)):
        count += 1 # Penambahan jumlah game yang terdaftar di data kepemilikan dengan 1
        if id == kepemilikan[i][0] and user_id == kepemilikan[i][1]:
            print('Anda sudah memiliki game tersebut!')
            return
        
    # Jika jumlah game sama dengan jumlah data kepemilikan maka lanjut ke proses pembelian
    if count == length(kepemilikan):
        # Looping untuk mencari indeks id game di data game
        for i in range(length(game)):
            if id == game[i][0]:
                # Validasi apakah jumlah stok game lebih dari 0
                if int(game[i][5]) > 0:
                    # Validasi apakah saldo yang dimiliki user lebih dari sama dengan harga game
                    if int(user[int(user_id)-1][5]) >= int(game[i][4]):
                        temp = [game[i][0],user_id] # Temporary array untuk ditambahkan ke data kepemilikan
                        today = str(datetime.today().year) # Untuk menambahkan data tahun pembelian
                        tempo = [game[i][0],game[i][1],game[i][4],user_id,today] # Temporary array untuk ditambahkan ke data riwayat
                        user[int(user_id)-1][5] = str(int(user[int(user_id)-1][5]) - int(game[i][4])) # Mengurangi saldo user dengan harga game
                        game[i][5] = str(int(game[i][5]) - 1) # Mengurangi stok game
                        kepemilikan += [temp] # Menambahkan temporary array ke data kepemilikan
                        history += [tempo] # Menambahkan temporary array ke data riwayat
                        print('Game',game[i][1],'berhasil dibeli!')
                        break
                    else:
                        print('Saldo anda tidak cukup untuk membeli game tersebut!')
                        break
                else:
                    print('Stok game tersebut sedang habis!')
                    break
