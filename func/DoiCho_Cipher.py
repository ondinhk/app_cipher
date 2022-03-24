def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]


def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    order = {
        int(val): num for num, val in enumerate(key)
    }
    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "")
    order = {
        int(val): num for num, val in enumerate(key)
    }
    plaintext = ''
    n = int(len(ciphertext) / len(key))
    for index in sorted(order.keys()):
        for part in split_len(ciphertext, n):
            try:
                plaintext += part[order[index]]
            except IndexError:
                continue
    return plaintext
