from .functions import*

# Cipher yang digunakan adalah Caesar Cipher dengan key +6
def cipher(password):
    temp = []
    for i in range(length(password)):
        temp += [ord(password[i])]
    for i in range(length(temp)):
        temp[i] = chr((temp[i] + 5 - 97) % 26 + 97)
    ciphered = ''
    for i in range(length(temp)):
        ciphered += temp[i]
    return ciphered

def uncipher(password):
    temp = []
    for i in range(length(password)):
        temp += [ord(password[i])]
    for i in range(length(temp)):
        temp[i] = chr((temp[i] - 5 - 97) % 26 + 97)
    ciphered = ''
    for i in range(length(temp)):
        ciphered += temp[i]
    return ciphered
