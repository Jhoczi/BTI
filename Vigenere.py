def GenerateVigenereKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range( len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def VigenereEncryption(text,key):
    nonAlpha = 0
    encrypted = ""
    for i in range(len(text)):
        if (text[i] == " "):
            encrypted +=" "
            nonAlpha += 1
        else:
            x = (ord(text[i]) + ord(key[i]) - nonAlpha) % 26
            x += ord('A')
            encrypted += chr(x)
    return encrypted

def VigenereDecryption(text,key):
    nonAlpha = 0
    decoded = ""
    for i in range(len(text)):
        if (text[i] == " "):
            decoded += " "
            nonAlpha += 1
        else:
            x = (ord(text[i]) - ord(key[i]) + 26 - nonAlpha) % 26
            x += ord('A')
            decoded += chr(x)
    return decoded

text = "filip to hultaj"
keyword = "AYUSH"

key = GenerateVigenereKey(text,keyword)
encryptedText = VigenereEncryption(text,key)
print(encryptedText)
decoded = VigenereDecryption(encryptedText, key)
print(decoded)