from .functions import*

def save(user,game,kepemilikan,history):
    user = arraytocsv(user)
    game = arraytocsv(game)
    kepemilikan = arraytocsv(kepemilikan)
    history = arraytocsv(history)

    dir = './saves/'
    os.chdir(dir)
    print('Disarankan : ' + str(datetime.today().replace(microsecond=0)))
    folder = input('Masukan nama folder penyimpanan: ')
    
    if not os.path.exists(folder):
        os.mkdir(folder)

    f = open(str(folder)+'/user.csv','w')
    f.write('id;username;nama;password;role;saldo\n')
    f.writelines(user)
    f.close
    f = open(str(folder)+'/game.csv','w')
    f.write('id;nama;kategori;tahun_rilis;harga;stok\n')
    f.writelines(game)
    f.close
    f = open(str(folder)+'/kepemilikan.csv','w')
    f.write('game_id;user_id\n')
    f.writelines(kepemilikan)
    f.close
    f = open(str(folder)+'/riwayat.csv','w')
    f.write('game_id;nama;harga;user_id;tahun_beli\n')
    f.writelines(history)
    f.close
