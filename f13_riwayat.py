from .functions import*

# Fungsi riwayat menerima parameter x dan y yaitu variabel history dan user_id
def riwayat(x,y):
    global history
    global user_id

    # Inisialisasi temporary array
    temp = []
    # Mengisi temporary array dengan elemen history
    # x[i][0] yaitu game_id, x[i][1] yaitu nama, x[i][2], yaitu kategori, x[i][3] yaitu tahun rilis, x[i][4] yaitu harga
    for i in range(length(x)):
        temp += [[x[i][0],x[i][1],x[i][2],x[i][3],x[i][4]]]

    if length(x) == 0: # Jika tidk memiliki game
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
            if y == temp[i][3]:
                # tempo[i][0] yaitu game_id, tempo[i][1] yaitu nama, tempo[i][2], yaitu kategori, tempo[i][3] yaitu tahun rilis, tempo[i][4] yaitu harga
                print(str(num[i]) + ' ' + temp[i][0] + ' | ' + temp[i][1] + ' | ' + temp[i][2] + ' | ' + temp[i][4])
