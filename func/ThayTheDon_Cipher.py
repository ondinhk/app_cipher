import random, sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(message, key):
    translated = ''
    charsA = LETTERS
    charsB = key
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated


def decrypt(message, key):
    translated = ''
    charsB = LETTERS
    charsA = key
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated


def getRandomKey():
    randomList = list(LETTERS)
    random.shuffle(randomList)
    return ''.join(randomList)


