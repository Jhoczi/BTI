import string

alphabet = string.ascii_lowercase

def CaesarEncryption(text, KEY):
    encrypted = ""
    for letter in text:
        if ord(letter) > 122 - KEY:
            encrypted += chr(ord(letter) + KEY - 26)
        else:
            encrypted += chr(ord(letter) + KEY)
    return encrypted

def CaeserDecoder(text, KEY):
    decoded = ""
    for letter in text:
        x = ord(letter)
        if (ord(letter))
        if (ord(letter) + KEY - 26) < 122:
            print(f'{letter}')
            decoded += chr(ord(letter) - KEY + 26)
        else:
            decoded += chr(ord(letter) - KEY)
    return decoded

KEY = 1
text = "az"
print(f'Teskt:\n{text}')
encrypted = CaesarEncryption(text,KEY)
print(f'Zaszyfrowany:\n{encrypted}')
decoded = CaeserDecoder(encrypted,KEY)
print(f'Odszyfrowany:\n{decoded}')