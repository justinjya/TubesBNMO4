from .f16_save import save

def exit(x,y,z,w):
    global user
    global game
    global kepemilikan
    global history

    inpt = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')

    if inpt == 'Y' or inpt == 'y':
        save(x,y,z,w)
        return
    elif inpt == 'N' or inpt == 'n':
        return