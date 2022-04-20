from .functions import*

# Fungsi login menerima parameter yaitu variabel user
def login(user):
    # Input username dan password
    username_login = input('Masukkan username: ')
    password_login = input('Masukkan password: ')

    # Looping untuk validasi apakah username dan password sesuai dengan data
    for i in range(length(user)):
        if username_login == user[i][1] and password_login == user[i][3]:
            print('Halo ' + user[i][2] + '! Selamat datang di "Binomo".')
            logged = True
            user_id = user[i][0]
            role = user[i][4]
            return logged, user_id, role
    else:
        logged = False
        user_id = ''
        role = ''
        print('Password atau username salah atau tidak ditemukan.') 
        return logged, user_id, role
