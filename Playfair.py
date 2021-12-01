def ConvertPlainTextToDiagraphs(plainText):
    for s in range(0, len(plainText) + 1, 2):
        if s < len(plainText) - 1:
            if plainText[s] == plainText[s + 1]:
                plainText = plainText[:s + 1] + 'X' + plainText[s + 1:]

    if len(plainText) % 2 != 0:
        plainText = plainText[:] + 'X'

    return plainText

def GenerateCipherKeyMatrix(key):
    matrix_5x5 = [[0 for i in range(5)] for j in range(5)]

    simpleKeyArr = []

    for c in key:
        if c not in simpleKeyArr:
            if c == 'J':
                simpleKeyArr.append('I')
            else:
                simpleKeyArr.append(c)

    isPies = "I" in simpleKeyArr
    isPiesExit = False

    for i in range(65,91):
        if chr(i) not in simpleKeyArr:
            if(i == 73 and not isPies):
                simpleKeyArr.append("I")
                isPiesExit = True
            elif i == 73 or i == 74 and isPiesExit:
                pass
            else:
                simpleKeyArr.append(chr(i))

    index = 0
    for i in range(0,5):
        for j in range(0,5):
            matrix_5x5[i][j] = simpleKeyArr[index]
            index += 1

    return matrix_5x5

def IndexLocator(char,cipherKeyMatrix):
    indexOfChar = []
    if char == "J":
        char = "I"

    for i,j in enumerate(cipherKeyMatrix):
        for k,l in enumerate(j):
            if char == l:
                indexOfChar.append(i)
                indexOfChar.append(k)
                return indexOfChar

def Encryption(planText,key):
    cipherText = []
    keyMatrix = GenerateCipherKeyMatrix(key)
    i = 0
    while i < len(planText):
        n1 = IndexLocator(planText[i],keyMatrix)
        n2 = IndexLocator(planText[i+1],keyMatrix)

        if n1[1] == n2[1]:
            i1 = (n1[0] + 1) % 5
            j1 = n1[1]

            i2 = (n2[0] + 1) % 5
            j2 = n2[1]

            cipherText.append(keyMatrix[i1][j1])
            cipherText.append(keyMatrix[i2][j2])
            cipherText.append(", ")
        elif n1[0] == n2[0]:
            i1 = n1[0]
            j1 = (n1[1] + 1) % 5

            i2 = n2[0]
            j2 = (n2[1] + 1) % 5
            cipherText.append(keyMatrix[i1][j1])
            cipherText.append(keyMatrix[i2][j2])
            cipherText.append(", ")
        else:
            i1 = n1[0]
            j1 = n1[1]

            i2 = n2[0]
            j2 = n2[1]

            cipherText.append(keyMatrix[i1][j2])
            cipherText.append(keyMatrix[i2][j1])
            cipherText.append(", ")
        i+=2
    return cipherText

def Decryption(planText, key):
    planText = planText.replace(" ","").replace(",","")
    result = []
    keyMatrix = GenerateCipherKeyMatrix(key)
    i = 0
    while i < len(planText):
        n1 = IndexLocator(planText[i], keyMatrix)
        n2 = IndexLocator(planText[i + 1], keyMatrix)

        if n1[1] == n2[1]:
            i1 = (n1[0] - 1) % 5
            j1 = n1[1]

            i2 = (n2[0] - 1) % 5
            j2 = n2[1]

            result.append(keyMatrix[i1][j1])
            result.append(keyMatrix[i2][j2])

        elif n1[0] == n2[0]:
            i1 = n1[0]
            j1 = (n1[1] -1) % 5

            i2 = n2[0]
            j2 = (n2[1] - 1) % 5
            result.append(keyMatrix[i1][j1])
            result.append(keyMatrix[i2][j2])

        else:
            i1 = n1[0]
            j1 = n1[1]

            i2 = n2[0]
            j2 = n2[1]

            result.append(keyMatrix[i1][j2])
            result.append(keyMatrix[i2][j1])
        i += 2
    return "".join(result)



text = "WESOLESZYFROWANIE"
key = "AMOGUS"
matrix = GenerateCipherKeyMatrix(key)
convertedText = ConvertPlainTextToDiagraphs(text)
encrypted = "".join(Encryption(convertedText,key))
decrypted = Decryption(encrypted,key)
print(f'Tablica: {matrix}')
print(f'Slowo: {text}')
print(f'Zakodowane: {encrypted}')
print(f'Odkodowane: {decrypted}')