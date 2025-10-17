import convert
import freq

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
        print(convert.arrayToString(cipher))
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
        print(convert.arrayToString(shifted),freq.dictValue(shifted),shift)
        diffs.append([shifted,freq.dictValue(cipher),shift])
    pointer = 0
    for j in range(len(diffs)):
        if diffs[j][1] > diffs[pointer][1]:
            pointer = j
    diffs[pointer][0] = convert.arrayToString(diffs[pointer][0])
    print("\n")
    print(diffs[pointer])