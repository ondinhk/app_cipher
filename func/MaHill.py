import numpy as np


def encrypt(msg, key):
    msg = msg.replace(" ", "")  # Thay the khoang trang
    K = make_key(key)  # Tao va Kiem tra Khoa
    len_check = len(msg) % 2 == 0
    if not len_check:
        msg += "0"
    P = create_matrix_of_integers_from_string(msg)  # Tach plaintext
    msg_len = int(len(msg) / 2)
    encrypted_msg = ""
    for i in range(msg_len):  # Ma hoa P*K
        row_0 = P[0][i] * K[0][0] + P[1][i] * K[0][1]
        integer = int(row_0 % 26 + 65)
        encrypted_msg += chr(integer)
        row_1 = P[0][i] * K[1][0] + P[1][i] * K[1][1]
        integer = int(row_1 % 26 + 65)
        encrypted_msg += chr(integer)
    return encrypted_msg


def decrypt(encrypted_msg, key):
    K = make_key(key)  # Tao va Kiem tra Khoa
    # Tinh dinh thuc
    determinant = K[0][0] * K[1][1] - K[0][1] * K[1][0]
    determinant = determinant % 26
    # Tinh nghich dao cua dinh thuc
    multiplicative_inverse = find_multiplicative_inverse(determinant)
    # Tinh ma tran nghich dao cua Khoa K
    K_inverse = K
    K_inverse[0][0], K_inverse[1][1] = K_inverse[1, 1], K_inverse[0, 0]
    K[0][1] *= -1
    K[1][0] *= -1
    for row in range(2):
        for column in range(2):
            K_inverse[row][column] *= multiplicative_inverse
            K_inverse[row][column] = K_inverse[row][column] % 26
    # Tach cipher text
    C = create_matrix_of_integers_from_string(encrypted_msg)
    msg_len = int(len(encrypted_msg) / 2)
    decrypted_msg = ""
    for i in range(msg_len):  # Giai ma C*K^-1
        column_0 = C[0][i] * K_inverse[0][0] + C[1][i] * K_inverse[0][1]
        integer = int(column_0 % 26 + 65)
        decrypted_msg += chr(integer)
        column_1 = C[0][i] * K_inverse[1][0] + C[1][i] * K_inverse[1][1]
        integer = int(column_1 % 26 + 65)
        decrypted_msg += chr(integer)
    if decrypted_msg[-1] == "0":
        decrypted_msg = decrypted_msg[:-1]
    return decrypted_msg


def find_multiplicative_inverse(determinant):  # Tim nghich dao dthuc
    multiplicative_inverse = -1
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse


def make_key(key):  # Tao va kiem tra khoa
    determinant = 0
    K = None
    while True:
        # KEY = input("Input 4 letter cipher: ")  # Nhap 4 ky tu cach nhau
        key = key.replace(" ", "")
        K = create_matrix_of_integers_from_string(key)
        determinant = K[0][0] * K[1][1] - K[0][1] * K[1][0]
        determinant = determinant % 26
        inverse_element = find_multiplicative_inverse(determinant)
        if inverse_element == -1:
            print("Determinant is not relatively prime to 26, uninvertible key")
        elif np.amax(K) > 26 and np.amin(K) < 0:
            print("Only a-z characters are accepted")
            print(np.amax(K), np.amin(K))
        else:
            break
    return K


def create_matrix_of_integers_from_string(string):  # Tao ma tran Khoa
    integers = [chr_to_int(c) for c in string]
    length = len(integers)
    M = np.zeros((2, int(length / 2)), dtype=np.int32)
    iterator = 0
    for column in range(int(length / 2)):
        for row in range(2):
            M[row][column] = integers[iterator]
            iterator += 1
    return M


def chr_to_int(char):
    char = char.upper()
    integer = ord(char) - 65
    return integer

if __name__ == "__main__":
    msg = input("Message: ")
    encrypted_msg = encrypt(msg)
    print(encrypted_msg)
    decrypted_msg = decrypt(encrypted_msg)
    print(decrypted_msg)
