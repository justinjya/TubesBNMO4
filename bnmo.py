import func

user, game, kepemilikan, history = func.load()
logged = False
user_id = ''
role = ''

print('Selamat datang di antarmuka "Binomo"')

while True :
    inpt = input('>>> ')
    if logged == True:
        if role == 'user':
            if inpt == 'buy_game':
                func.buy_game(user,game,kepemilikan,history,user_id)
            elif inpt == 'list_game':
                func.list_game(game,kepemilikan,user_id)
            elif inpt == 'search_my_game':
                func.search_my_game(game,kepemilikan,user_id)
            elif inpt == 'riwayat':
                func.riwayat(history,user_id)
            elif inpt == 'list_game_toko':
                func.list_game_toko(game)
            elif inpt == 'search_game_at_store':
                func.search_game_at_store(game)
            elif inpt == 'help':
                func.help(logged,role)
            elif inpt == 'save':
                func.save(user,game,kepemilikan,history)
            elif inpt == 'kerangajaib':
                func.kerangajaib()
            elif inpt == 'tictactoe':
                func.tictactoe()
            elif inpt == 'exit':
                func.exit(user,game,kepemilikan,history)
                break
            else:
                print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.') 
        elif role == 'admin':
            if inpt == 'register':
                func.register(user)
            elif inpt == 'tambah_game':
                func.tambah_game(game)
            elif inpt == 'ubah_game':
                func.ubah_game(game)
            elif inpt == 'ubah_stok':
                func.ubah_stok(game)
            elif inpt == 'topup':
                func.topup(user)
            elif inpt == 'list_game_toko':
                func.list_game_toko(game)
            elif inpt == 'search_game_at_store':
                func.search_game_at_store(game)
            elif inpt == 'help':
                func.help(logged,role)
            elif inpt == 'save':
                func.save(user,game,kepemilikan,history)
            elif inpt == 'kerangajaib':
                func.kerangajaib()
            elif inpt == 'tictactoe':
                func.tictactoe()
            elif inpt == 'exit':
                func.exit(user,game,kepemilikan,history)
                break
            else:
                print('Maaf, anda harus menjadi User untuk melakukan hal tersebut')
    else:
        if inpt == 'login':
            logged, user_id, role = func.login(user)
        elif inpt == 'help':
            func.help(logged,role)
        elif inpt == 'exit':
            func.exit(user,game,kepemilikan,history)
        elif inpt == 'kerangajaib':
            func.kerangajaib()
        elif inpt == 'tictactoe':
            func.tictactoe()
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login" dan "help".')
