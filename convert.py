def stringToArray(string):
    array = []
    for char in range(len(string)):
        array.append(string[char])
    return array

def arrayToString(array,spaces):
    string = ""
    for item in range(len(array)):
        if spaces:
            string += array[item]
        else:
            if array[item] != " ":
                string += array[item]
    return string

# for solving use