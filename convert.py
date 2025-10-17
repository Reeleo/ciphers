def stringToArray(string):
    array = []
    for char in range(len(string)):
        array.append(string[char])
    return array

def arrayToString(array):
    string = ""
    for item in range(len(array)):
        string += array[item]
    return string
