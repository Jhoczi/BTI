def GenerateVigenereKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range( len(string) - len(key)):
            key.append(key[i % len(key)].upper())
    return ''.join(key)

def VigenereEncryption(text,key):
    encrypted = ""
    for i in range(len(text)):
        if (ord(text[i]) == 32):
            encrypted += " "
            continue
        x = (ord(text[i].upper()) + ord(key[i])) % 26
        x += ord('A')
        encrypted += chr(x)
    return encrypted

def VigenereDecryption(text,key):
    nonAlpha = 0
    decoded = ""
    for i in range(len(text)):
        if (ord(text[i]) == 32):
            decoded += " "
            continue
        x = (ord(text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        decoded += chr(x)
    return decoded

text = "siema siema siema"
keyword = "AZ"


key = GenerateVigenereKey(text,keyword)
encryptedText = VigenereEncryption(text,key)
decoded = VigenereDecryption(encryptedText, key)
print(f'Tekst:{text}')
print(f'Slowo kluczowe:{keyword}')
print(f'Klucz:{key}')
print(f'Zakodowany: {encryptedText}')
print(f'Odkodowany: {decoded}')