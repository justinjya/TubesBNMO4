from .functions import*

def register(x):
    global user
    
    simbol = ['-','_']
    nomor = ['1','2','3','4','5','6','7','8','9','0']
    big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    nama = input('Masukkan nama: ')
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')

    for i in range(length(x)):
        if username == x[i][1]:
            print('Username', username, 'sudah terpakai, silahkan menggunakan username lain')
            break
    else:
        count = 0

        temp = [0 for i in range(length(username))]
        for i in range(length(username)):
            temp[i] = username[i]

        for i in range(length(username)):
            if length(username) < 5:
                print('Username harus memiliki minimal 5 karakter')
                break
            else:
                for i in range(length(username)):
                    if (temp[i] in big) or (temp[i] in small) or (temp[i] in simbol) or (temp[i] in nomor):
                        count += 1
                if count == length(username):
                    print('Username', username, 'telah berhasil register ke dalam "Binomo".')
                    temp = [length(x)+1, username, nama, password, 'user', 0]
                    x += [temp]
                    break
                else:
                    print('Username hanya dapat mengandung huruf besar, huruf kecil, angka 0-9, underscore "_", dan strip "_"')
                    break