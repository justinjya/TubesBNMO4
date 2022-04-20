from .f16_save import save

# Fungsi exit menerima parameter yaitu variabel user, game, kepemilikan, dan history
def exit(user,game,kepemilikan,history):
    # Input iya atau tidak
    inpt = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')

    # Jika iya maka menjalankan fungsi save
    if inpt == 'Y' or inpt == 'y':
        save(user,game,kepemilikan,history)
        return
    elif inpt == 'N' or inpt == 'n':
        return
