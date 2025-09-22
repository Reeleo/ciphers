






def ceasar(cipher):
    array = []
    for char in range(len(cipher)):
        array.append(cipher[char])
    shifted = []
    for i in range(24):
        for j in range(len(array)):
            ascii = ord(array[j])
            array[j] == ascii+1
            
    return array












ciphertxt = input("cipher text: ")
print(ceasar(ciphertxt))