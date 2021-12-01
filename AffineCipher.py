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
        return None  # modular inverse does not exist
    else:
        return x % m

def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])

def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([ chr((( ModInv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])

    # declaring text and key
    text = 'AFFINE CIPHER'
    key = [17, 20]

    # calling encryption function
    affine_encrypted_text = affine_encrypt(text, key)

    print('Encrypted Text: {}'.format(affine_encrypted_text))

    # calling decryption function
    print('Decrypted Text: {}'.format
          (affine_decrypt(affine_encrypted_text, key)))




# alphabetText = list("aąbcćdeęfghijklłmnńoópqrsśtuvwyzźż")
#
# def CreateCodedAlphabet(a,b,alphabet):
#     result = set()
#     for i in range(len(alphabet)):
#         result.add( alphabet[((a * i) + b) % len(alphabet)] )
#     return result
#
# def AffineCipher(text, alphabet, codedAlphabet):
#     encoded = ""
#     for letter in text:
#         letter = letter.lower()
#         if letter == " ":
#             encoded += " "
#         else:
#             for j in range(len(alphabet)):
#                 if letter == alphabet[j]:
#                     encoded += codedAlphabet.get(j)
#     return encoded
#
# def AffineDecode(text, alphabet, codedAlphabet):
#     decoded = ""
#     for letter in text:
#         letter = letter.lower()
#         if letter == " ":
#             decoded += " "
#         else:
#             for j in range(len(alphabet)):
#                 if letter == codedAlphabet.get(j):
#                     decoded += alphabet[j]
#     return decoded
#
# a = 2
# b = 1
# text = "super tajne haslo"
# codedAlphabet = CreateCodedAlphabet(a,b,alphabetText)
# codedText = AffineCipher(text,alphabetText,codedAlphabet)
# decodedText = AffineDecode(codedText,alphabetText,codedAlphabet)
# print(f'Coded Alphabet: {codedAlphabet}')
# print(f'Coded text: {text}')
# print(f'Encoded Text: {codedText}')
# print(f'Decoded Text: {decodedText}')
#

