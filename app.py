from flask import Flask, render_template, request
import main

app = Flask(__name__)
result = ""
arr_cipher = ["Reverse Cipher",
              "Caesar Cipher",
              "Mã đổi chổ",
              "Mã thay thế",
              "Mã Affine",
              "Mã Vigenere",
              "Mã Hill"]


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def translate():
    global result
    # Request form
    # Get text
    text = request.form["input_text"]
    text = text.upper()
    text = text.replace(" ", "")
    # Get cipher
    cipher = request.form["cipher"]
    # Get endrypt or decrypt
    option = request.form["option"]

    # Key Caesar:
    key = request.form["input_key"]
    # Key doi cho
    key_doicho = request.form["input_key_doicho"]
    # Key thay the
    key_thaythe = request.form["input_key_thaythedon"]
    if key_thaythe == '':
        key_thaythe = main.getkey_thaythedon()
    # Key Vigenere
    key_vigenere = request.form["input_key_vigenere"]
    key_vigenere = key_vigenere.replace(" ", "")
    key_vigenere = key_vigenere.upper()

    # Convert option
    cipher = int(cipher)
    option = int(option)
    key = int(key)
    # Encrypt == 0
    if option == 0:
        # Reverse
        if cipher == 0:
            result = main.en_reverse(text)
        # Ceasar:
        if cipher == 1:
            result = main.en_ceasar(text, key=key)
            arr_cipher[1] = "Caesar Cipher, Key=" + str(key)
        # Doi cho:
        if cipher == 2:
            result = main.en_doicho(text, key=key_doicho)
            arr_cipher[2] = "Mã đổi chổ, Key=" + key_doicho
        # Thay the:
        if cipher == 3:
            result = main.en_thaythedon(text, key=key_thaythe)
            arr_cipher[3] = "Mã thay thế, Key=" + key_thaythe
        # Affine
        if cipher == 4:
            result = main.en_affine(text)
        # Vigenere
        if cipher == 5:
            result = main.en_vigenere(text, key_vigenere)
            arr_cipher[5] = "Mã Vigenere, Key=" + key_vigenere
        # Hill
        if cipher == 6:
            result = main.en_hill(text, key_vigenere)
            arr_cipher[6] = "Mã Hill, Key=" + key_vigenere


    # Decrypt
    elif option == 1:
        # Reverse:
        if cipher == 0:
            result = main.de_reverse(text)
        # Ceasar:
        if cipher == 1:
            result = main.de_ceasar(text, key=key)
        # Doi cho:
        if cipher == 2:
            result = main.de_doicho(text, key=key_doicho)
            arr_cipher[2] = "Mã đổi chổ, Key=" + key_doicho
        # Thay the:
        if cipher == 3:
            result = main.de_thaythedon(text, key=key_thaythe)
            arr_cipher[3] = "Mã thay thế, Key=" + key_thaythe
        # Affine
        if cipher == 4:
            result = main.de_affine(text)
        # Vigenere
        if cipher == 5:
            result = main.de_vigenere(text, key_vigenere)
            arr_cipher[5] = "Mã Vigenere, Key=" + key_vigenere
        # Hill
        if cipher == 6:
            result = main.de_hill(text, key_vigenere)
            arr_cipher[6] = "Mã Hill, Key=" + key_vigenere
    return render_template("index.html", cipher=arr_cipher[cipher], result=result, input=text)


if __name__ == '__main__':
    app.run(debug=True)
