# Ma dao nguoc


def encrypt(message):
    i = len(message) - 1
    translated = ''
    while i >= 0:
        translated = translated + message[i]
        i = i - 1
    return translated


def decrypt(translated):
    i = len(translated) - 1
    decrypted = ''
    while i >= 0:
        decrypted = decrypted + translated[i]
        i = i - 1
    return decrypted
