import base64

sample_string = input('Enter the text you want to encrypt: ') #"GeeksForGeeks is the best"
sample_string_bytes = sample_string.encode("ascii")
 
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

base64_string2 = base64_string #" R2Vla3NGb3JHZWVrcyBpcyB0aGUgYmVzdA =="
base64_bytes2 = base64_string2.encode("ascii")
  
sample_string_bytes = base64.b64decode(base64_bytes2)
sample_string = sample_string_bytes.decode("ascii")
  
print(f"Encoded string: {base64_string}")
print(f"Decoded string: {sample_string}")
