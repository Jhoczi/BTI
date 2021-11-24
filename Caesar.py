
def CaesarEncryption(text, KEY):
    encrypted = ""
    for letter in text:
        letter = str.lower(letter)
        newValue = (ord(letter) -97 + KEY) % 26
        if (ord(letter) == 32):
            encrypted += " "
        else:
            encrypted += chr(newValue + 97)
    return encrypted

def CaeserDecoder(text,KEY):
    decoded = ""
    for letter in text:
        letter = str.lower(letter)
        newValue = (ord(letter) - 97 - KEY) % 26
        if (ord(letter) == 32):
            decoded += " "
        else:
            decoded += chr(newValue + 97)
    return decoded

KEY = 13
text = "testowo zaszyfrowane zdanie"
print(f'Teskt:\n{text}')
encrypted = CaesarEncryption(text,KEY)
print(f'Zaszyfrowany:\n{encrypted}')
decoded = CaeserDecoder(encrypted,KEY)
print(f'Odszyfrowany:\n{decoded}')
