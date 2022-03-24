def mod_inverse(x, m):
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break
        elif n == m - 1:
            return "Null"
        else:
            continue


class Affine(object):
    DIE = 26
    KEY = (7, 3, mod_inverse(7, 26))

    def __init__(self):
        pass

    # def set_key(self,):

    def encryptChar(self, char):
        K1, K2, kI = self.KEY
        return chr((K1 * (ord(char) - 65) + K2) % self.DIE + 65)

    def encrypt(self, string):
        return "".join(map(self.encryptChar, string))

    def decryptChar(self, char):
        K1, K2, KI = self.KEY
        return chr(KI * ((ord(char) - 65) - K2) % self.DIE + 65)

    def decrypt(self, string):
        return "".join(map(self.decryptChar, string))

#
# affine = Affine()
# p = 'ONAUGUST'
# c = affine.encrypt(p)
# print (affine.KEY)
# print (c)
# print(affine.decrypt(c))
