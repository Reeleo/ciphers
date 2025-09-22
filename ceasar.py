



def dictionary(txt):
    diff = 0
    engdict = {"a":8.2,"b":1.5,"c":2.8,"d":4.3,"e":12.7,"f":2.2,"g":2.0,"h":6.1,"j":0.15,"k":0.77,
               "l":4.0,"m":2.4,"n":6.7,"o":7.5,"p":1.9,"q":0.095,"r":6.0,"s":6.3,"t":9.1,"u":2.8,
               "v":0.98,"w":2.4,"x":0.15,"y":2.0,"z":0.074}
    newdict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"j":0,"k":0,
               "l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,
               "v":0,"w":0,"x":0,"y":0,"z":0}  
    
    for char in range(len(txt)):
        for letter in newdict:
            if txt[char] == letter:
                newdict[letter] += 1
                break
    for i in newdict:
        newdict[i] = newdict[i] / len(txt)
    
    for j in newdict:
        if newdict[j] > 0:
            diff += abs(engdict[j] - newdict[j])
    return round(diff,2)








def ceasar(cipher):
    array = []
    diffs = []
    cipher.lower()
    for char in range(len(cipher)):
        array.append(cipher[char])
    for shift in range(26):
        for i in range(len(array)):
            if array[i] != " ":
                ascii = ord(array[i])
                if ascii+1 >= 123:
                    ascii = 96
                array[i] = chr(ascii+1)
        #print(array,dictionary(array))
        diffs.append([array,dictionary(array),shift])
    pointer = 0
    for j in range(len(diffs)):
        if diffs[j][1] > diffs[pointer][1]:
            pointer = j
        elif diffs[j][1] == diffs[pointer][1]:
            print(diffs[pointer])
            pointer = j
    return diffs[pointer]













ciphertxt = input("cipher text: ")
print(ceasar(ciphertxt))

