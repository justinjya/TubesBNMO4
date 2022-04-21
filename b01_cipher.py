from .functions import*

# Cipher yang digunakan adalah Caesar Cipher dengan key +6
def cipher(password):
    temp = [ord(i) for i in password]
    for i in range(length(temp)):
        temp[i] = chr((temp[i] + 5 - 97) % 26 + 97)
    ciphered = ''
    for i in range(length(temp)):
        ciphered += temp[i]
    return ciphered

def uncipher(password):
    temp = [ord(i) for i in password]
    for i in range(length(temp)):
        temp[i] = chr((temp[i] - 5 - 97) % 26 + 97)
    unciphered = ''
    for i in range(length(temp)):
        unciphered += temp[i]
    return unciphered