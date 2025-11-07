#becca
FREQ = {"a":8.2,"b":1.5,"c":2.8,"d":4.3,"e":12.7,"f":2.2,"g":2.0,"h":6.1,"i":7.0,"j":0.15,
            "k":0.77,"l":4.0,"m":2.4,"n":6.7,"o":7.5,"p":1.9,"q":0.095,"r":6.0,"s":6.3,"t":9.1,
            "u":2.8,"v":0.98,"w":2.4,"x":0.15,"y":2.0,"z":0.074}

list_chars = []


class message:
    def __init__(self,message):
        self.list = []

    def make_list(self,message):
        for char in message:
            self.list.append(char)


    
message1 = message('fse  fs')
print('fse  fs'.strip())
print(message1.list)
count = 0

message4a = 'WINOK BVYBN NOBLI SWECD KNWSD DYCYW OMYXP ECSYX KPDOB BOKNS XQIYE BVODD OBKCS MKXXY DMVOK BVICO ORYGS WSQRD LOYPK XIKCC SCDKX MODYI YEZOB RKZCD RKDCR YGCKG KXDYP SWKQS XKDSY XYXWI ZKBDL EDSDB EVIPK SVDYC OORYG KXIDR SXQSM YEVNN YGYEV NRKFO DROVO KCDSX PVEOX MOEZY XDROQ BOKDK PPKSB CXYGC DSBBS XQKMB YCCDR OYMOK XIYEK BOAES DOBSQ RDDRK DGOCR KBOKN OOZNS CVSUO YPDRK DNBOK NPEVS XCDSD EDSYX CVKFO BIKXN SBOTY SMONK CIYEN SNKDD ROFSM DYBSO CYPWB VSXMY VXKXN DROXO GRYZO DROIL BSXQD YCYWK XIVYX QCEPP OBSXQ ZOYZV OIODS MKXXY DLOVS OFODR KDKXI DRSXQ SWSQR DGBSD OYBCK IMYEV NWYFO DROMY XQBOC CYBDR OZBOC SNOXD DYGKB NCKTE CDMYE BCOSP IYEBY GXOPP YBDCR KFOXY DKVBO KNIZO BCEKN ONDRO WXYXO DROVO CCWBL KLLKQ OSCWY CDSXC SCDOX DDRKD SCRYE VNROK BIYEB CMROW OKXNS GSVVL OSXVY XNYXX OHDGO OUPYB KWOOD SXQYP DROQR YCDMV ELSPI YEKBO GSVVS XQGOW SQRDW OODDR OBOYB SPIYE ZBOPO BKAES ODOBC ODDSX QKDDR OKDRO XOEWS BOWKS XWINO KBVYB NNOBL IFOBI DBEVI IYEBC MRKBV OCNSM UOXC'
message4a = message4a.lower()
# message3a = 'FW MHLEBGY REHLH, B UHP HQ NBLPQ JEOHPOM HGM QZOG HEHLFOM QI LOROBTO WISL EOQQOL. ZHJJW IN RISLPO QI DGIU QZHQ WIS ZHTO HLLBTOM PHNOEW BG GOU WILD HGM QZOG HEHLFOM HQ WISL HRRISGQ IN QZO ASLGOM GIQO. B UHP PQSGY AW H MHLD JHGY IN COHEISPW, NOHLBGY QZHQ BQ FBYZQ AO H EOQQLO M\’HFISL. RISEM BQ AO QZO LOHPIG QZHQ ZO MBM GIQ HEEIU FO QI HRRIFJHGW ZBF QI GOU WILD? B HF JLISM QI PHW QZHQ B MBPFBPPOM QZBP UBRDOM QZISYZQ HP SGUILQZW IN SP AIQZ HGM UHP SGPSLJLBPOM QZISYZ, B FSPQ RIGNOPP, H EBQQEO LOEBOTOM QI LOHM WISL OVJEHGHQBIG IN QZO BMOGQBQW IN QZO POGMOL. QZO FWPQOLW LOFHBGP HP QI UZHQ ASPBGOPP QZO YOGOLHE ZHM UBQZ FW AOEITOM, HGM UZW ZO ZHP RZIPOG QI RIFFSGBRHQO UBQZ RZHLEOP BG RIMO. B PSJJIPO BQ FBYZQ AO RIGGORQOM UBQZ RZHLEOP’P FOOQBGY UBQZ FL AHAAHYO HGM QZO JLBFO FBGBPQOL IG QZO MHW AONILO ZO EONQ. QZO MIIL QI QZO PQSMW UHP REIPOM, ASQ TIBROP UOLO REOHLEW LHBPOM MSLBGY QZO MBPRSPPBIG HGM RZHLEOP UHP BG H QOLLBAEO FIIM HNQOLUHLMP. ZO UISEM IGEW PHW QZHQ ZO UHP “QII IEM QI AO BGTIETOM BG PDSEMSYYOLW!” BN GIQ, QZOG B PSJJIPO QZHQ QZO EOQQOL FBYZQ ZHTO RIGROLGOM QZO HRQBTBQBOP IN QZO YZIPQ RESA. BP QZHQ QII NHGRBNSE? UZBEO QZO PIRBOQW BP ZHLMEW PORLOQ, PIFO JLHRQBRHE FOG HLO MBPFBPPBTO IN HG BGQOLOPQ BG PJBLBQSHEBPF, HGM B RHG BFHYBGO QZHQ H FHG UZI ZHP FHMO ZBP LOJSQHQBIG HP HG OGYBGOOL FHW NOOE QZHQ PSRZ HG HPPIRBHQBIG UISEM MHFHYO ZBP PQHGMBGY. BP QZOLO HGW UHW QZHQ WIS RISEM HPROLQHBG QZO RIGQOGQP IN QZBP RILLOPJIGMOGRO, IL QZO GHQSLO IN QZO LOEHQBIGPZBJ AOQUOOG QZOF? B HF FIPQ RSLBISP QI EOHLG. WISLP HNNORQBIGHQOEW, OEEOG'
# message3a = message3a.lower()

print(message4a)

def make_list(message):
    list = []
    for i in message:
        if i != ' ' and i != ',' :
            list.append(i)
    return list

def bubble_sort(list,pos):
    for i in range (len(list)):
        for j in range(len(list)-i-1):
            if list[j][pos] > list[j+1][pos] :
                holder = list[j+1]
                list[j+1] = list[j]
                list[j] = holder
    return list

def substitute (list, key):
    message = ''
    for i in range (26):
        for j in range(len(list)):
            if list[j] == key[i][0]:
                list[j] = key[i][1].upper()
    for i in list:
        message += i 
    print(message)
    return(message)

def rearrange(list,key):
    message = ''
    for j in range (len(list)//(len(key))):
        # original = []
        # for i in range (len(key)):
        #     original.append(list[j*len(key)+i])
        for i in range (len(key)):
            pos = key[i]
            message += list[j*len(key)+pos] 
    print('why',message)

def create_rearragements(list,key_length):
    key = []
    for a in range (key_length):
        key.append(a)
        for b in range (key_length):
            key.append(b)
            for c in range (key_length):
                key.append(c)
                for d in range (key_length):
                    key.append(d)
                    for e in range (key_length):
                        key.append(e)
                        for f in range (key_length):
                            key.append(f)
                        # print(key)
                            if (key.count(0) == 1 or key.count(0) == 0) and (key.count(1) == 1 or key.count(1) == 0) and (key.count(2) == 1 or key.count(2) == 0) and (key.count(3) == 1 or key.count(3) == 0) and (key.count(4) == 1 or key.count(4) == 0) and (key.count(5) == 1 or key.count(5) == 0) and (key.count(6) == 1 or key.count(6) == 0) and (key.count(7) == 1 or key.count(8) == 0):
                                rearrange(list,key)
                            key.pop()
                        key.pop()
                    key.pop()
                key.pop()
            key.pop()
        key.pop()
    print('huhhh', count)

def letter_frequency(list):
    a = ord('a')
    real_frequency = []
    frequency_list = []
    difference = 0
    key = []
    
    real_frequency_dict = {"a":8.2,"b":1.5,"c":2.8,"d":4.3,"e":12.7,"f":2.2,"g":2.0,"h":6.1,"i":7.0,"j":0.15,
            "k":0.77,"l":4.0,"m":2.4,"n":6.7,"o":7.5,"p":1.9,"q":0.095,"r":6.0,"s":6.3,"t":9.1,
            "u":2.8,"v":0.98,"w":2.4,"x":0.15,"y":2.0,"z":0.074}
    frequency_dict = {"a":8.2,"b":1.5,"c":2.8,"d":4.3,"e":12.7,"f":2.2,"g":2.0,"h":6.1,"i":7.0,"j":0.15,
            "k":0.77,"l":4.0,"m":2.4,"n":6.7,"o":7.5,"p":1.9,"q":0.095,"r":6.0,"s":6.3,"t":9.1,
            "u":2.8,"v":0.98,"w":2.4,"x":0.15,"y":2.0,"z":0.074}
    for i in range (26):
        ascii = a + i
        letter = chr(ascii)
        frequency = list.count(letter)
        real_frequency.append([letter,frequency_dict[letter]])
        frequency_dict[letter] =frequency/len(list) * 100
        frequency_list.append([letter,frequency/len(list) * 100])

    print(frequency_dict)
    print()
    real_frequency = bubble_sort(real_frequency,1)
    frequency_list = bubble_sort(frequency_list,1)
    print(frequency_list)
    for i in range (26):
        difference = abs(real_frequency[i][1] - frequency_list[i][1])
        key.append([frequency_list[i][0],real_frequency[i][0] ])
    print(difference) 
    print(key)
        # print(letter,':',frequency)
print(letter_frequency(make_list(message4a)))
message = substitute(make_list(message4a),[['j', 'z'], ['h', 'q'], ['a', 'j'], ['t', 'x'], ['u', 'k'], ['f', 'v'], ['l', 'b'], ['z', 'p'], ['g', 'g'], ['m', 'y'], ['q', 'f'], ['p', 'm'], ['w', 'w'], ['i', 'c'], ['e', 'u'], ['n', 'l'], ['v', 'd'], ['r', 'r'], ['c', 'h'], ['x', 's'], ['b', 'n'], ['s', 'i'], ['k', 'o'], ['y', 'a'], ['d', 't'], ['o', 'e']])
shortened4a = make_list('WCLEONDANLLENBCIWUHTOLWITTAHAWEYASMUHIASOMTENNEOLISFCAUNDETTENOHIYOSSATYDEONDCHEERAGIWIFRTBEAMOSCOHHIHTOSYETACAUPENROPHTROTHRAGHOGOSTAMIWOFISO')
create_rearragements(shortened4a, 6)

# print(letter_frequency(make_list(message3a)))
