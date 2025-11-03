import math

'''
aaa = []
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
'''
combo = []
combos = []
answers = []
for i in range (25):
    combo.append(i)
    for j in range (61):
        combo.append(j)
        for k in range (61):
            combo.append(k)
            # print(combo)
            if combo[0]-combo[1] == combo[1]-combo[2] and combo[1]-combo[2] != 0:
                # print(combo)
                total = combo[0] * 3600 + combo[1] * 60 + combo[2]
                hour = total/120 % 360
                min = total/10 % 360
                sec= total*6 % 360
                ans = abs(hour - min) + abs(min - sec) + abs(sec - hour)
                answers.append(ans)
                if ans == 8.600000000000364:
                    print(combo)
            combo.pop()
        combo.pop()
    combo.pop()
# print(answers)
smallest = 99999
for ans in answers:
    if ans < smallest:
        smallest = ans

        print(smallest)