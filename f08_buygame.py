from .functions import*

# Fungsi buy_game menerima parameter x, y, z, w, q yaitu varibael user, game, kepemilikan, history, user_id
def buy_game(x,y,z,w,q):
    global user
    global game
    global kepemilikan
    global history
    global user_id

    # Input id game
    id = input('Masukkan ID game: ')
    # Inisialisasi jumlah game yang ada di data kepemilikan
    count = 0

    # Looping untuk validasi apakah user_id sudah memiliki id game
    for i in range(length(z)):
        count += 1 # Penambahan jumlah game yang terdaftar di data kepemilikan dengan 1
        if id == z[i][0] and q == z[i][1]:
            print('Anda sudah memiliki game tersebut!')
            return
        
    # Jika jumlah game sama dengan jumlah data kepemilikan maka lanjut ke proses pembelian
    if count == length(z):
        # Looping untuk mencari indeks id game di data game
        for i in range(length(y)):
            if id == y[i][0]:
                # Validasi apakah jumlah stok game lebih dari 0
                if int(y[i][5]) > 0:
                    # Validasi apakah saldo yang dimiliki user lebih dari sama dengan harga game
                    if int(x[int(q)-1][5]) >= int(y[i][4]):
                        temp = [y[i][0],q] # Temporary array untuk ditambahkan ke data kepemilikan
                        today = str(datetime.today().year) # Untuk menambahkan data tahun pembelian
                        tempo = [y[i][0],y[i][1],y[i][4],q,today] # Temporary array untuk ditambahkan ke data riwayat
                        x[int(q)-1][5] = str(int(x[int(q)-1][5]) - int(y[i][4])) # Mengurangi saldo user dengan harga game
                        y[i][5] = str(int(y[i][5]) - 1) # Mengurangi stok game
                        z += [temp] # Menambahkan temporary array ke data kepemilikan
                        w += [tempo] # Menambahkan temporary array ke data riwayat
                        print('Game',y[i][1],'berhasil dibeli!')
                        break
                    else:
                        print('Saldo anda tidak cukup untuk membeli game tersebut!')
                        break
                else:
                    print('Stok game tersebut sedang habis!')
                    break
