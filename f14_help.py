# Fungsi help menerima parameter yaitu variabel logged dan role
def help(logged,role):
    # Jika belum login
    if logged == False:
        print('============ HELP ============')
        print('1. login - Untuk melakukan login ke dalam sistem')
        print('2. help - Untuk melihat daftar perintah yang dapat dijalankan program.')
        print('3. exit - Untuk keluar dari program.')
    else:
        # Jika role yaitu admin
        if role == 'admin':
            print('============ HELP ============')
            print('1. register - Untuk melakukan registrasi user baru')
            print('2. login - Untuk melakukan login ke dalam sistem')
            print('3. tambah_game - Untuk menambah game yang dijual pada toko')
            print('4. ubah_game - Untuk mengubah informasi game yang dijual pada toko')
            print('5. ubah_stok - Untuk mengubah jumlah stok game yang dijual pada toko.')
            print('6. list_game_toko - Untuk melihat lis game yang dijual pada toko')
            print('7. search_game_at_store - Untuk melihat lis game yang dijual pada toko berdasarkan kriteria pencarian.')
            print('8. topup - Untuk menambahkan/mengurangi saldo kepada User.')
            print('9. save - Untuk menyimpan data ke dalam file setelah dilakukan perubahan.')
            print('10. help - Untuk melihat daftar perintah yang dapat dijalankan program.')
            print('11. exit - Untuk keluar dari program.')
            
        # Jika role yaitu user
        elif role == 'user':
            print('============ HELP ============')
            print('1. login - Untuk melakukan login ke dalam sistem')
            print('2. list_game_toko - Untuk melihat lis game yang dijual pada toko')
            print('3. buy_game - Untuk membeli game pada toko')
            print('4. list_game - Untuk melihat lis game yang dimiliki User.')
            print('5. search_my_game - Untuk melihat lis game yang dimiliki User berdasarkan kriteria pencarian.')
            print('6. search_game_at_store - Untuk melihat lis game yang dijual pada toko berdasarkan kriteria pencarian.')
            print('7. riwayat - Melihat riwayat pembelian game pada User.')
            print('8. save - Untuk menyimpan data ke dalam file setelah dilakukan perubahan.')
            print('9. help - Untuk melihat daftar perintah yang dapat dijalankan program.')
            print('10. exit - Untuk keluar dari program.')
