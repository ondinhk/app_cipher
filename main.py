import func.Reverse_Cipher as reverse
import func.Ceasar_Cipher as ceasar
import func.DoiCho_Cipher as doicho
import func.ThayTheDon_Cipher as thaythe
import func.MaAffine as affine
import func.MaVigenere as vigenere
import func.MaHill as hill
import func.Base64 as base64
import func.MaRSA as rsa


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


# Base64:
def en_base64(text):
    return base64.encodeBase64(text)


def de_base64(text):
    return base64.decodeBase64(text)


# RSA
def createKey():
    return rsa.createKey()


def en_RSA(text, pathfile):
    return rsa.en_code(text, pathfile)


def de_RSA(text, pathfile):
    return rsa.de_code(text, pathfile)


if __name__ == '__main__':
    pathPub = "./Key/publicKey.pem"
    pathPri = "./Key/privateKey.pem"
    text = "ondinhkhang"
    enn = b'{S\x9b_\x05\xb6+\xac\x10\xcdb\x03\xf3A\xe8\x94Y\xec\xd7w\x8c\x93\x80\xd3Rc\xa1\xc6\x83kO\r\xa6c\xc7\xb4(\xb3\xaf/NS\x9a\xb7\xe0\xd2\xbb\x95\xcf\x81=\xcf\x08!\xd8\xef\xeb;\xe5\x15<D+,;\xb6L\x87\x904\xd2J\x84D\x11\xf1\x1e_\xb8\xcc\x1c=\x1f\xa3\xf2\xf4l\x17\xb7\xec\xf7,\x97\xa7\xf6\x91\x12\xb9T\xbb\x86\x9d\xf9q,\xdbZ\xa9\x06@A\x83\xef\xa7IDV\xa1\xf9\xc8\xf9\xf1q+af\x0fN$X\xc6\xbc\xceu\x19\xfe\x14~\xf3 >)w_kS\x9d]_\x8f\xbe\x8eW\x02\xab(\x02\x8f]\x98{]{&v\xe3\xd6.\x9f\x84\x98#z-\x16^<\xcd\x8d\xd2\x0fb>\x1c\x9b\xec\x96\x8f\x1c\xd3IX\x80V\x86\xf9J-u\xe7\xc4!\x16\xe6\xc6U\xcf\x92O\x94\x82x^F\xba\xacCX\x81\xac\x0bm\xcav,7\xbe\xaec\xe08\xd0\xe4\x05\x1c\xb7\x85\\\x05-\xa2\xa2\x84\xfc*]\xf6\x0b\x8a\x90P\x14O\xe3r\xb5'
    en = en_RSA(text,pathPub)
    de = de_RSA(enn,pathPri)
    # print(en)
    print(de)
