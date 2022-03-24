import sys
import base64

from itertools import cycle


if sys.version_info[0] < 3: # if python 2
    from itertools import izip

    def _encode_string(string):
        return base64.encodestring(string)

    def _decode_string(string):
        return base64.decodestring(string)
else:
    izip = zip

    def _encode_string(string):
        return base64.encodebytes(string.encode()).decode()

    def _decode_string(string):
        return base64.decodebytes(string.encode()).decode()


key = 'nguyenNgoc'

def _xored(value, key):
    return chr(ord(value) ^ ord(key))


def xor(data, keys):
    data_pair = izip(data, cycle(keys))
    return ''.join(_xored(val, key) for (val, key) in data_pair)


def decode(data, keys=key):
    data_decoded = _decode_string(data)
    return xor(data_decoded, keys)


def encode(data, keys=key):
    data_xored = xor(data, keys)
    return _encode_string(data_xored).replace('\n', '')


if __name__ == "__main__":

    keys = input('Enter the key you want to encrypt: ') #'s3cre7-h45h'
    text = input('Enter the text you want to encrypt: ') #'this is secret text 1@#@#/host:port'
    
    enc = encode(text, keys)
    dec = decode(enc, keys)
    
    print('text:{}\nencode:"{}"\ndecode:{}'.format(text, enc, dec))
