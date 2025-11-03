import math

# ---------- Question 1 --------- #
'''
sum = 0
for i in range(1,9):
    for j in range(10,21):
        for k in range(1,10):
            num = (str(i)+str(j)+str(k))
            sum += int(num)
print(sum)
#3686760


tum = 0
for i in range(1,9):
    for j in range(10,21):
        for k in range(1,10):
            num = (i*1000*j*10*k)
            tum += int(num)
print(tum)
#2673000000

print(sum/tum)
#0.0013792592592592593
#0.001379
'''
# ---------- Question 1 --------- #


# ---------- Question 6 --------- #
'''
# original 4,3,-2,4,3,-5

def reset():
    return 4,3,-2,4,3,-5


many = 1
if many == 0:
    ax,ay,bx,by,cx,cy = reset()
    for i in range(6):
        ax,ay,bx,by,cx,cy = reset()
        for j in range(4000000):
            point = (j-2000000)/100000
            # print(point)
            if i == 0:
                ii = "ax"
                ax = point
            elif i == 1:
                ii = "ay"
                ay = point
            elif i == 2:
                ii = "bx"
                bx = point
            elif i == 3:
                ii = "by"
                by = point
            elif i == 4:
                ii = "cx"
                cx = point
            elif i == 5:
                ii = "cy"
                cy = point


            ab = (ax-bx)**2+(ay-by)**2
            rootab = math.sqrt(ab)

            bc = (bx-cx)**2+(by-cy)**2
            rootbc = math.sqrt(bc)

            ca = (cx-ax)**2+(cy-ay)**2
            rootca = math.sqrt(ca)

            if ab+bc == ca:
                print("RA",ii,point,"  area:",round(rootab*rootbc/2,3))
            elif bc+ca == ab:
                print("RA",ii,point,"  area:",round(rootbc*rootca/2,3))
            elif ab+ca == bc:
                print("RA",ii,point,"  area:",round(rootab*rootca/2,3))
elif many == 1:
    ax,ay,bx,by,cx,cy = reset()

    ab = (ax-bx)**2+(ay-by)**2
    rootab = math.sqrt(ab)
    #print(ab)

    bc = (bx-cx)**2+(by-cy)**2
    rootbc = math.sqrt(bc)
    #print(bc)

    ca = (cx-ax)**2+(cy-ay)**2
    rootca = math.sqrt(ca)
    #print(ca)

    if ab+bc == ca:
        print("RA")
        print(round(rootab*rootbc/2,3))
    elif bc+ca == ab:
        print("RA")
        print(round(rootbc*rootca/2,3))
    elif ab+ca == bc:
        print("RA")
        print(round(rootab*rootca/2,3))
elif many == 2:
    ra = False
    ax,ay,bx,by,cx,cy = reset()
    abM = (ay-by) / (ax-bx)
    bcM = (by-cy) / (bx-cx)
    caM = (cy-ay) / (cx-ax)
    
    print(round(abM,5),round(bcM,5),round(caM,5))
    if abM != 0:
        if -1 / abM == bcM or -1 / abM == caM:
            print("rightangle")
            print(round(abM,5),round(bcM,5),round(caM,5))
            ra = True
    else:
        if bcM == 0 or caM == 0:
            print("rightangle")
            print(round(abM,5),round(bcM,5),round(caM,5))
            ra = True


    if bcM != 0:
        if -1 / bcM == abM or -1 / bcM == caM:
            print("rightangle")
            print(round(abM,5),round(bcM,5),round(caM,5))
            ra = True
    else:
        if abM == 0 or caM == 0:
            print("rightangle")
            print(round(abM,5),round(bcM,5),round(caM,5))
            ra = True


    if caM != 0:
        if -1 / caM == abM or -1 / caM == bcM:
            print("rightangle")
            print(round(abM,5),round(bcM,5),round(caM,5))
            ra = True
    else:
        if abM == 0 or caM == 0:
            print("rightangle")
            print(round(abM,5),round(bcM,5),round(caM,5))
            ra = True
    
    ab = (ax-bx)**2+(ay-by)**2
    rootab = math.sqrt(ab)

    bc = (bx-cx)**2+(by-cy)**2
    rootbc = math.sqrt(bc)

    ca = (cx-ax)**2+(cy-ay)**2
    rootca = math.sqrt(ca)
    
    if ra:
        print(rootab,rootbc,rootca)
        if rootab > rootbc and rootab > rootca:
            area = rootbc*rootca/2
        elif rootbc > rootab and rootbc > rootca:
            area = rootab*rootca/2
        elif rootca > rootab and rootca > rootbc:
            area = rootab*rootbc/2
        print("area",area)
elif many == 3:
    areas = []
    ax,ay,bx,by,cx,cy = reset()
    for i in range(6):
        ax,ay,bx,by,cx,cy = reset()
        for j in range(40000):
            ra = False
            point = (j-20000)/1000
            if i == 0:
                ii = "ax"
                ax = point
            elif i == 1:
                ii = "ay"
                ay = point
            elif i == 2:
                ii = "bx"
                bx = point
            elif i == 3:
                ii = "by"
                by = point
            elif i == 4:
                ii = "cx"
                cx = point
            elif i == 5:
                ii = "cy"
                cy = point

            if ax-bx != 0:
                abM = (ay-by) / (ax-bx)
            if bx-cx != 0:
                bcM = (by-cy) / (bx-cx)
            if cx-ax != 0:
                caM = (cy-ay) / (cx-ax)
            

            if abM != 0:
                if -1 / abM == bcM or -1 / abM == caM:
                    #print("rightangle")
                    #print(round(abM,5),round(bcM,5),round(caM,5))
                    ra = True
            else:
                if bcM == 0 or caM == 0:
                    #print("rightangle")
                    #print(round(abM,5),round(bcM,5),round(caM,5))
                    ra = True


            if bcM != 0:
                if -1 / bcM == abM or -1 / bcM == caM:
                    #print("rightangle")
                    #print(round(abM,5),round(bcM,5),round(caM,5))
                    ra = True
            else:
                if abM == 0 or caM == 0:
                    #print("rightangle")
                    #print(round(abM,5),round(bcM,5),round(caM,5))
                    ra = True


            if caM != 0:
                if -1 / caM == abM or -1 / caM == bcM:
                    #print("rightangle")
                    #print(round(abM,5),round(bcM,5),round(caM,5))
                    ra = True
            else:
                if abM == 0 or bcM == 0:
                    #print("rightangle")
                    #print(round(abM,5),round(bcM,5),round(caM,5))
                    ra = True
            
            ab = (ax-bx)**2+(ay-by)**2
            rootab = math.sqrt(ab)

            bc = (bx-cx)**2+(by-cy)**2
            rootbc = math.sqrt(bc)

            ca = (cx-ax)**2+(cy-ay)**2
            rootca = math.sqrt(ca)
            
            if ra:
                #print(rootab,rootbc,rootca)
                if rootab > rootbc and rootab > rootca:
                    area = rootbc*rootca/2
                elif rootbc > rootab and rootbc > rootca:
                    area = rootab*rootca/2
                elif rootca > rootab and rootca > rootbc:
                    area = rootab*rootbc/2
                areas.append(["AREA",round(area,3),":",ax,ay,bx,by,cx,cy])
    print(areas)
'''
# ---------- Question 6 --------- #




# ---------- Question 7 --------- #
def checkArithmetic(h,m,s):
    hmDiff = m-h
    msDiff = s-m
    if hmDiff == msDiff:
        return hmDiff
    else:
        return 0
    
def makeAccute(angle):
    if angle > 180:
        return 360-angle
    return angle

totals = []
for h in range(25):
    for m in range(61):
        for s in range(61):
            d = checkArithmetic(h,m,s)
            over12 = False
            if d != 0:
                if h > 12:
                    h -= 12
                    over12 = True
                hangle = h*30+m*0.5+s*(1/120)
                mangle = m*6+s*0.1
                sangle = s*6
                alpha = makeAccute(abs(hangle-mangle))
                beta = makeAccute(abs(mangle-sangle))
                gamma = makeAccute(abs(hangle-sangle))
                total = alpha+beta+gamma
                if over12:
                    d += 12
                if total < 50:
                    totals.append([round(total,2),": h",h,round(hangle,3),"m",m,round(mangle,3),"s",s,round(sangle,3)])

totals.sort(key=lambda x: x[0],reverse=True)
for i in range(len(totals)):
    print(totals[i])

# ---------- Question 7 --------- #

