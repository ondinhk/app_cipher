import func.Reverse_Cipher as reverse
import func.Ceasar_Cipher as ceasar
import func.DoiCho_Cipher as doicho
import func.ThayTheDon_Cipher as thaythe
import func.MaAffine as affine
import func.MaVigenere as vigenere
import func.MaHill as hill

# Reverse:
def en_reverse(text):
    return reverse.encrypt(text)


def de_reverse(text):
    return reverse.decrypt(text)


# Ceasar:
def en_ceasar(text, key):
    return ceasar.encrypt(text, k=key)


def de_ceasar(text, key):
    return ceasar.decrypt(text, k=key)


# Mã đổi chổ:
def en_doicho(text, key):
    return doicho.encrypt(text, key=key)


def de_doicho(text, key):
    return doicho.decrypt(text, key=key)


# Mã thay thế đơn:
def en_thaythedon(text, key):
    return thaythe.encrypt(text, key)


def de_thaythedon(text, key):
    return thaythe.decrypt(text, key)


def getkey_thaythedon():
    return thaythe.getRandomKey()


# Mã Affine
def en_affine(text):
    object = affine.Affine()
    return object.encrypt(text)


def de_affine(text):
    object = affine.Affine()
    return object.decrypt(text)


# Mã Vigenere:
def en_vigenere(text, key):
    return vigenere.encrypt(text, key=key)


def de_vigenere(text, key):
    return vigenere.decrypt(text, key=key)

# Mã hill:
def en_hill(text, key):
    return hill.encrypt(text, key=key)


def de_hill(text, key):
    return hill.decrypt(text, key=key)
if __name__ == '__main__':
    text = 'ondinhkhang'
    text = text.upper()
    key = "abc"
    # c = en_doicho(text, key)
    c = en_vigenere(text,key)
    print(c)
    print(de_vigenere(c,key))
