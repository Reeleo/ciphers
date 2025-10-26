FREQ = {"a":8.2,"b":1.5,"c":2.8,"d":4.3,"e":12.7,"f":2.2,"g":2.0,"h":6.1,"i":7.0,"j":0.15,
            "k":0.77,"l":4.0,"m":2.4,"n":6.7,"o":7.5,"p":1.9,"q":0.095,"r":6.0,"s":6.3,"t":9.1,
            "u":2.8,"v":0.98,"w":2.4,"x":0.15,"y":2.0,"z":0.074}




def dictValue(txt):
    diff = 0
    newdict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,
               "k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,
               "u":0,"v":0,"w":0,"x":0,"y":0,"z":0}   
    for char in range(len(txt)):
        for letter in newdict:
            if txt[char] == letter:
                newdict[letter] += 1
                break
    for i in newdict:
        newdict[i] = newdict[i] / len(txt)
    
    for j in newdict:
        if newdict[j] > 0:
            diff += abs(FREQ[j] - newdict[j])
    return round(diff,2)


def freqLetters(txt):
    letters = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,
               "k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,
               "u":0,"v":0,"w":0,"x":0,"y":0,"z":0}  
    for char in range(len(txt)):
        for letter in letters:
            if txt[char] == letter:
                letters[letter] += 1
                break
    for i in letters:
        letters[i] = round(letters[i] / len(txt),2)
    letterSort = dict(sorted(letters.items(), key=lambda x:x[1], reverse=True))
    return letterSort
    

def freqWords(txt):
    words = {}
    word = ""
    for i in range(len(txt)):
        if txt[i] != " ":
            word += txt[i] 
        else:
            if word in words:
                words[word] += 1
            else:
                words.update({word:1})
            word = ""
    wordSort = dict(sorted(words.items(), key=lambda x:x[1], reverse=True))
    return wordSort









