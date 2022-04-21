from .functions import*

def kerangajaib():
    # Untuk menghasilkan seed secara acak dengan LCG
    x = (time.time()*1000)%60
    a = 3
    c = 1
    m = 5
    lcg = round(((a * x) + c) % m)
    
    # Input pertanyaan dan kondisi jawaban yang mungkin
    input('Apa pertanyaanmu? ')
    if lcg == 0:
        print('Ya.')
    elif lcg == 1:
        print('Tidak.')
    elif lcg == 2:
        print('Bisa jadi.')
    if lcg == 3:
        print('Mungkin.')
    elif lcg == 4:
        print('Tentunya.')
    elif lcg == 5:
        print('Tidak mungkin.')
