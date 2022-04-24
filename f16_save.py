from .functions import*

# Fungsi save menerima parameter yaitu variabel user, game, kepemilikan, dan history
def save(user,game,kepemilikan,history):
    # Mengubah array menjadi string untuk di - write ke file csv
    user = arraytocsv(user)
    game = arraytocsv(game)
    kepemilikan = arraytocsv(kepemilikan)
    history = arraytocsv(history)

    # Memasukkan nama folder penyimpanan file csv
    dir = './'
    os.chdir(dir)
    folder = input('Masukan nama folder penyimpanan: ')
    
    if not os.path.exists(folder):
        os.mkdir(folder) # Membuat folder baru jika nama folder tidak ditemukan

    # Mengisi file csv
    f = open('saves/' + str(folder) + '/user.csv','w')
    f.write('id;username;nama;password;role;saldo\n')
    f.writelines(user)
    f.close
    f = open('saves/' + str(folder) + '/game.csv','w')
    f.write('id;nama;kategori;tahun_rilis;harga;stok\n')
    f.writelines(game)
    f.close
    f = open('saves/' + str(folder) + '/kepemilikan.csv','w')
    f.write('game_id;user_id\n')
    f.writelines(kepemilikan)
    f.close
    f = open('saves/' + str(folder) + '/riwayat.csv','w')
    f.write('game_id;nama;harga;user_id;tahun_beli\n')
    f.writelines(history)
    f.close
    
    print('Saving...')
    print('Data telah tersimpan pada folder', folder)
