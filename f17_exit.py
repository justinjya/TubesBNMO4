from .f16_save import save

# Fungsi exit menerima parameter x, y, z, dan w yaitu variabel user, game, kepemilikan, dan history
def exit(x,y,z,w):
    global user
    global game
    global kepemilikan
    global history

    # Input iya atau tidak
    inpt = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')

    # Jika iya maka menjalankan fungsi save
    if inpt == 'Y' or inpt == 'y':
        save(x,y,z,w)
        return
    elif inpt == 'N' or inpt == 'n':
        return
