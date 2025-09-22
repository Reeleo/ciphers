


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


def setUp(cipher):
    cipher = cipher.lower()
    cipher = stringToArray(cipher)
    counter = 0
    valid = False
    while not valid:
        ascii = ord(cipher[counter])
        if ascii < 97 or ascii > 123:
            cipher.pop(counter)
        else:
            counter += 1
        if counter == len(cipher):
            valid = True
    cipher = arrayToString(cipher)
    return cipher



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
    array = stringToArray(cipher)
    for shift in range(26):
        for i in range(len(array)):
            if array[i] != " ":
                ascii = ord(array[i])
                if ascii+1 >= 123:
                    ascii = 96
                array[i] = chr(ascii+1)
        #print(array,dictionary(array),shift,"\n")
        shifted = []
        for j in range(len(array)):
            shifted.append(array[j])
        diffs.append([shifted,dictionary(array),shift])
    pointer = 0
    for j in range(len(diffs)):
        if diffs[j][1] > diffs[pointer][1]:
            pointer = j
    diffs[pointer][0] = arrayToString(diffs[pointer][0])
    return diffs[pointer]












a = "GUR ANGVBANY NEPUVIRF VA XRJ PBAGNVA N GUBHFNAQ LRNEF BS UVFGBEL. QBPHZRAGF BS FGNGR QNGVAT ONPX BIRE N GUBHFNAQ LRNEF NER PNERSHYYL CERFREIRQ NAQ FGHQVRQ OL UVFGBEVNAF SEBZ NEBHAQ GUR JBEYQ – SVYRF GUNG NER BSGRA FRAFVGVIR NAQ ZNEXRQ JVGU N ERYRNFR QNGR JUVPU PBHYQ OR NF YBAT NF BAR UHAQERQ LRNEF SBE CNEGVPHYNEYL FRAFVGVIR VASBEZNGVBA. ZHPU YRFF JRYY XABJA VF GUR FUNQBJ NEPUVIR, QRRC VAFVQR GUR UBZR BS OEVGVFU PBQROERNXVAT JUVPU PBAGNVAF SVYRF GUNG ZVTUG ARIRE OR ERYRNFRQ. GURL PNEEL GUR ZNEX QGN, JUVPU QRABGRF QRYRTNGR GB NEPUNRBYBTL, GUR GRNZ ERFCBAFVOYR SBE GURZ OHG GUR NEPUVIVFGF WBXR GUNG VG FGBBQ SBE QBA\’G GRYY NALBAR. GURFR SVYRF PBAGNVA FRPERGF GUNG, NYBAT JVGU GURVE PVCURE XRLF, JRER YBFG YBAT NTB. AB-BAR XABJF JUNG GERNFHERF GURL ZVTUG PBAGNVA. VG VF LBHE WBO GB OERNX GUR PVCUREF NAQ GB SVAQ BHG!"
b = "EDCT OEEW VAKUE DZK U OUXX BAHJ JOA ZEO KACLYEZJH NAG QAL JA KECUBTEG. JTEQ DGE JDWEZ NGAY JTE DGCTUMEH TEGE DJ IAHH CEZJGDX DZK GEXDJE JA EMEZJH ACCLGGUZS AMEG AZE TLZKGEK DZK NUNJQ QEDGH DSA. U TDME D NEEXUZS JTDJ JTEQ YUSTJ HJUXX IE GEXEMDZJ!!! QALG JDHW UH JA KECGQBJ EDCT AN JTE KACLYEZJH DZK LBXADK QALG HAXLJUAZH AZ JTE CTDXXEZSE BDSEH. UN QAL YDWE D YUHJDWE QAL OUXX SEJ HAYE NEEKIDCW DZK CDZ JGQ DSDUZ. QAL OUXX SEJ D HCAGE NAG EDCT DJJEYBJ DZK OE OUXX ILUXK D XEDKEGIADGK LHUZS JTAHE HCAGEH. UN QAL DGE UZ D JEDY, JTEZ AZXQ JTE JEDY CDBJDUZ CDZ LBXADK HLIYUHHUAZH, HA YDWE HLGE QAL OAGW OUJT JTEY JA SEJ QALG DZHOEGH HLIYUJJEK. UZ QALG DCCALZJ BDSEH QAL OUXX NUZK D GECAGK AN QALG HLIYUHHUAZH, JASEJTEG OUJT D CABQ AN D CEGJUNUCDJE GECAGKUZS QALG BGASGEHH. UN QAL ODZJ QAL CDZ DXXAO QALG JEDCTEG JA NAXXAO QALG BGASGEHH IQ SEJJUZS JTE JEDY CDBJDUZ JA EZJEG D HBECUDX BUZ ZLYIEG (JTE JEDCTEG\’H YAZUJAGUZS BUZ) UZJA JTE JEDY KEJDUXH AZ JTEUG DCCALZJ BDSE. UN QAL TDME DZQ FLEHJUAZH JTEZ TEDK AMEG JA JTE NAGLY OTEGE QAL OUXX NUZK XAJH AN NGUEZKXQ DKMUCE! SAAK XLCW, TDGGQ"

a = setUp(a)
b = setUp(b)

print(ceasar(a))

