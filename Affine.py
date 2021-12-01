def ExtendedEuclideanAlgorithm(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def ModInv(a, m):
    gcd, x, y = ExtendedEuclideanAlgorithm(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def AffineEncryption(text, KEY):
    result = []
    for t in text.upper().replace(' ', ''):
        coded = (( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')
        result.append( chr(coded))
    return ''.join(result)


def AffineDecryption(text,KEY):
    result = []
    for c in text:
        decoded = (( ModInv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')
        result.append(chr(decoded))
    return ''.join(result)


text = "Moj przykladowy test"
key = [17,20]

encryptedText = AffineEncryption(text,key)
decryptedText = AffineDecryption(encryptedText,key)

print(f'Text: {text}')
print(f'Encrypted text: {encryptedText}')
print(f'Decrypted text: {decryptedText}')