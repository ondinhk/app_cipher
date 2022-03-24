#8/
#Bai tap 1:
def encrypt(text,k):
    text = text.replace(" ","")
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + k - 65) % 26 + 65)
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)
    return result
def decrypt(text,k):
    text = text.replace(" ","")
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - k - 65) % 26 + 65)
        else:
            result += chr((ord(char) - k - 97) % 26 + 97)
    return result
#text = ""
text = input('Enter the text you want to encrypt: ')
k = 13
#print ("Key = : " ,k)
c = encrypt(text,k)
print ("Cipher text: ", c )
print ("Plain text: ", decrypt(c,k))
