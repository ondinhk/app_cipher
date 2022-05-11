import base64


def encodeBase64(text):
    mess_byte = text.encode('ascii')
    base64_bytes = base64.b64encode(mess_byte)
    return base64_bytes.decode('ascii')


def decodeBase64(text):
    plain_bytes = base64.b64decode(text)
    return plain_bytes.decode('ascii')


if __name__ == '__main__':
    x = encodeBase64("Onkhang")
    print(x)
    y = decodeBase64(x)
    print(y)
