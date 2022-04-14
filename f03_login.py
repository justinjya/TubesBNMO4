from .functions import*

def login(x):
    global logged
    global user
    global user_id
    global role

    username_login = input('Masukkan username: ')
    password_login = input('Masukkan password: ')

    for i in range(length(x)):
        if username_login == x[i][1] and password_login == x[i][3]:
            print('Halo ' + x[i][2] + '! Selamat datang di "Binomo".')
            logged = True
            user_id = x[i][0]
            role = x[i][4]
            return logged, user_id, role
    else:
        logged = False
        user_id = ''
        role = ''
        print('Password atau username salah atau tidak ditemukan.') 
        return logged, user_id, role