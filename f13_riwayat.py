from .functions import*

# Fungsi riwayat menerima parameter yaitu variabel history dan user_id
def riwayat(history,user_id):
    # Inisialisasi temporary array
    temp = []
    # Mengisi temporary array dengan elemen history
    # history[i][0] yaitu game_id, history[i][1] yaitu nama, history[i][2] yaitu kategori, history[i][3] yaitu tahun rilis, history[i][4] yaitu harga
    for i in range(length(history)):
        if user_id == history[i][3]:
            temp += [[history[i][0],history[i][1],history[i][2],history[i][4]]]

    if length(history) == 0: # Jika tidk memiliki game
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah "buy_game" untuk membeli.')
    else:
        for i in range(length(x[0])):
            spaces(temp,i)
        num = [0 for i in range(length(temp))]
        for i in range(length(num)):
            num[i] = i+1
        numSpaces(num)
        print('Daftar game:')
        # Output daftar game dalam riwayat pembelian sesuai user_id
        for i in range(length(temp)):
                # tempo[i][0] yaitu game_id, tempo[i][1] yaitu nama, tempo[i][2], yaitu kategori, tempo[i][3] yaitu tahun rilis, tempo[i][4] yaitu harga
                print(str(num[i]) + ' ' + temp[i][0] + ' | ' + temp[i][1] + ' | ' + temp[i][2] + ' | ' + temp[i][3])
