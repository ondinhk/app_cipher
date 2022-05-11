from flask import Flask, render_template, request, send_file
import main
import os
import time

app = Flask(__name__)
result = ""
app.config['UPLOAD_FOLDER'] = "/home/onkhang/PycharmProjects/ATBMTT/Upload"
arr_cipher = ["Reverse Cipher",
              "Caesar Cipher",
              "Mã đổi chổ",
              "Mã thay thế",
              "Mã Affine",
              "Mã Vigenere",
              "Mã Hill",
              "Mã Base64"]

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/rsa', methods=['POST'])
def rsatrang():
    # Get form
    # Get text, Option
    text = request.form["input_text"]
    text = text.replace(" ", "")
    # Get endrypt or decrypt
    option = request.form["option"]

    # Create key if correct
    create = request.form["create_key"]
    if int(create) == 0:
        main.rsa.createKey()
        linkPublic = "/download/public"
        linkPrivate = "/download/private"
        return render_template("resultKey.html", linkPublic=[linkPublic, "Link download publicKey"],
                               linkPrivate=[linkPrivate, "Link download privateKey"])

    # Kiểm tra có tệp được gửi lên không
    # File input
    if request.files:
        # Nhận file -> file key
        fileKey = request.files['keyfile']
        # Lấy đường dẫn trong máy
        pathFile = os.path.join(app.config['UPLOAD_FOLDER'], fileKey.filename)
        # Lưu file vào địa chỉ UPLOAD_FOLDER
        fileKey.save(pathFile)
        time.sleep(1)
        # option 1 is encode
        if int(option) == 0:
            output = main.en_RSA(text, pathFile)
            return render_template("rsa.html", result=output, input=text)
        # option != 1 is decode
        elif int(option) == 1:
            text = bytes(text, 'utf-8')
            print(type(text))
            output = main.de_RSA(text, pathFile)
            return render_template("rsa.html", result=output, input=text)
    return render_template("rsa.html", result=text)


@app.route('/download/public')
def download_file_public():
    pathPublic = "Key/publicKey.pem"
    return send_file(pathPublic, as_attachment=True)


@app.route('/download/private')
def download_file_private():
    pathPrivate = "Key/privateKey.pem"
    return send_file(pathPrivate, as_attachment=True)


@app.route('/', methods=['POST'])
def translate():
    global result
    # Request form
    # Get cipher
    cipher = request.form["cipher"]

    # Get text
    text = request.form["input_text"]
    text = text.replace(" ", "")

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

    # upper text
    if cipher != 7:
        text = text.upper()
    if cipher == 8:
        return render_template("rsa.html")
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
        # Base64
        if cipher == 7:
            result = main.en_base64(text)

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
        # Base64
        if cipher == 7:
            result = main.de_base64(text)

    return render_template("index.html", cipher=arr_cipher[cipher], result=result, input=text)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
