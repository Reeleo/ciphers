aa = []
aaa.append(2)
print(aaa)
list = []
for a in range (6):
    list.append(a+1)
    for b in range (6):
        list.append(b+1)
        for c in range (6):
            list.append(c+1)
            for d in range (6):
                list.append(d+1)
                for e in range (6):
                    list.append(e+1)
                    if 2 in list and 5 in list:
                        #print(list)
                        count += 1
                    list.pop()
                list.pop()
            list.pop()
        list.pop()
    list.pop()
print(count)