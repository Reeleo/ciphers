import convert
import freq

# guesses some letters for you for substitution but not very helpful
def findKey(cipher,type,key):
    letters = convert.frequencyLetters(cipher)
    words = convert.frequencyWords(cipher)

    if type == "l":
        print(letters)
    else:
        print(words)

    if type == "l":
        orderDict = sorted(freq.FREQ.items(), key=lambda x:x[1], reverse=True)
        orderTxt = dict(sorted(letters.items(), key=lambda x:x[1], reverse=True))
        print(orderDict)
        print(orderTxt)
        count = 0
        for i in orderTxt:
            oldletter = i
            newletter = orderDict[count][0]
            count += 1
            key[newletter] = oldletter
        return key
        
    
    if type == "w":
        freq_a = 0
        freq_i = 0
        freq_the = 0
        suspect_the = "the"
        suspect_a = "a"
        suspect_i = "i"
        for item in words:
            if len(item) == 1:
                if words[item] > freq_i:
                    suspect_a = suspect_i
                    suspect_i = item
                    freq_a = freq_i
                    freq_i = words[item]
                elif words[item] > freq_a and words[item] <= freq_i:
                    suspect_a = item
                    freq_a = words[item]
                #pepe
            elif len(item) == 3:
                if words[item] > freq_the:
                    suspect_the = item
                    freq_the = words[item]
        print(suspect_the, freq_the, ": suspected the")
        print(suspect_a, freq_a, ": suspected a")
        print(suspect_i, freq_i, ": suspected i")
        key[suspect_a] = "a"
        key["a"] = suspect_a
        key[suspect_i] = "i"
        key["i"] = suspect_i
        key[suspect_the[0]] = "t"
        key["t"] = suspect_the[0]
        key[suspect_the[1]] = "h"
        key["h"] = suspect_the[1]
        key[suspect_the[2]] = "e"
        key["e"] = suspect_the[2]
        print(key)
        return key


# requires alphabet key (function findkey is to help but not very helpful) trial and error guessing time
def substitution(cipher,k):
    again = True
    #type = input("words or letters ")
    print(freq.freqWords(cipher))
    print("\n")
    print(freq.freqLetters(cipher))
    while again:
        #key = findKey(cipher,type,k)
        key = k
        print("KEY: ",key)
        originalDiff = freq.dictValue(cipher)
        for char in range(len(cipher)):
            if cipher[char] != " ":
                i = cipher[char]
                cipher[char] = key[i]

        print(freq.dictValue(cipher),"from",originalDiff)
        print(convert.arrayToString(cipher,True))
        print("\n")
        print(freq.freqWords(cipher))
        print("\n")
        print(freq.freqLetters(cipher))
        again = False
        #y = input("again? ")
        # if y == "n":
        #     again = False
        # elif y == "s":
        #     if type == "w":
        #         type = "l"
        #     else:
        #         type = "w"

# substitution when the spaces are jumbled
def sSubstitution(cipher,k):
    print(freq.freqWords(cipher))
    print("\n")
    print(freq.freqLetters(cipher))
    key = k
    print("KEY: ",key)
    originalDiff = freq.dictValue(cipher)
    for char in range(len(cipher)):
        if cipher[char] != " ":
            i = cipher[char]
            cipher[char] = key[i]

    print(freq.dictValue(cipher),"from",originalDiff)
    print(convert.arrayToString(cipher,False))
    print("\n")
    print(freq.freqLetters(cipher))



# the vigenere chart shift (not done in challenge yet)
def vigenere(cipher):
    k = "hello"
    key = []
    for i in range(len(k)):
        key.append(ord(k[i]) - 97)
    print(key)
    pointer = 0
    for j in range(len(cipher)):
        if cipher[j] != " ":
            ascii = ord(cipher[j])
            if ascii+key[pointer] >= 123:
                diff = ascii+key[pointer] - 122
                ascii = 96 + diff
            else:
                ascii += key[pointer]
            cipher[j] = chr(ascii)
            pointer += 1
            if pointer >= len(key):
                pointer = 0
    print(cipher)

# vigenere but auto key (is made from the plain/cipher? text)
def vAutokey(cipher):
    k = "hello"
    key = []
    for i in range(len(k)):
        key.append(ord(k[i]) - 97)
    print(key)
    pointer = 0
    for j in range(len(cipher)):
        if cipher[j] != " ":
            ascii = ord(cipher[j])
            key.append(ascii-97)
            if ascii+key[pointer] >= 123:
                diff = ascii+key[pointer] - 122
                ascii = 96 + diff
            else:
                ascii += key[pointer]
            cipher[j] = chr(ascii)
            pointer += 1
    print(key)
    print(cipher)
            

# ciphertxt = abcde, key = [5,4,3,2,1], plaintxt = edcba (will have a similar dictvalue to english)
# solves if the right key is inputed
def transposition(cipher,key):
    pointer = 0
    splitcipher = [[]]
    for i in range(len(cipher)):
        if cipher[i] != " ":
            splitcipher[pointer].append(cipher[i])
            if len(splitcipher[pointer]) == len(key):
                splitcipher.append([])
                pointer += 1
    transposed = ""
    for j in range(len(splitcipher)):
        newgroup = ""
        if len(splitcipher[j]) == len(key):
            for k in range(len(key)):
                newgroup += splitcipher[j][key[k]]
            transposed += newgroup
    print(transposed)



# finds the most likely shift and solves
def ceasar(cipher):
    diffs = []
    for shift in range(26):
        for i in range(len(cipher)):
            if cipher[i] != " ":
                ascii = ord(cipher[i])
                if ascii+1 >= 123:
                    ascii = 96
                cipher[i] = chr(ascii+1)
        shifted = []
        for j in range(len(cipher)):
            shifted.append(cipher[j])
        print("\n")
        print(convert.arrayToString(shifted,True),freq.dictValue(shifted),shift)
        diffs.append([shifted,freq.dictValue(cipher),shift])
    pointer = 0
    for j in range(len(diffs)):
        if diffs[j][1] > diffs[pointer][1]:
            pointer = j
    diffs[pointer][0] = convert.arrayToString(diffs[pointer][0],True)
    print("\n")
    print(diffs[pointer])