
FREQ = {"a":8.2,"b":1.5,"c":2.8,"d":4.3,"e":12.7,"f":2.2,"g":2.0,"h":6.1,"i":7.0,"j":0.15,
            "k":0.77,"l":4.0,"m":2.4,"n":6.7,"o":7.5,"p":1.9,"q":0.095,"r":6.0,"s":6.3,"t":9.1,
            "u":2.8,"v":0.98,"w":2.4,"x":0.15,"y":2.0,"z":0.074}

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
        if cipher[counter] != " ":
            if ascii < 97 or ascii > 123:
                cipher.pop(counter)
            else:
                counter += 1
        else:
            counter += 1
        if counter == len(cipher):
            valid = True
    return cipher



def dictionary(txt):
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



def frequencyLetters(txt):
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
    return letters
    

def frequencyWords(txt):
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
    return words





def findKey(cipher,type):
    key = {"a":"a","b":"b","c":"c","d":"d","e":"e","f":"f","g":"g","h":"h","i":"i","j":"j","k":"k",
        "l":"l","m":"m","n":"n","o":"o","p":"p","q":"q","r":"r","s":"s","t":"t","u":"u",
        "v":"v","w":"w","x":"x","y":"y","z":"z"}  
    letters = frequencyLetters(cipher)
    words = frequencyWords(cipher)

    if type == "l":
        print(letters)
    else:
        print(words)

    if type == "l":
        orderDict = sorted(FREQ.items(), key=lambda x:x[1], reverse=True)
        orderTxt = dict(sorted(letters.items(), key=lambda x:x[1], reverse=True))
        print(orderDict)
        print(orderTxt)
        count = 0
        for i in orderTxt:
            oldletter = i
            newletter = orderDict[count][0]
            count += 1
            key[newletter] = oldletter
        return key
        
    
    if type == "w":
        freq_a = 0
        freq_i = 0
        freq_the = 0
        suspect_the = "the"
        suspect_a = "a"
        suspect_i = "i"
        for item in words:
            if len(item) == 1:
                if words[item] > freq_i:
                    suspect_a = suspect_i
                    suspect_i = item
                    freq_a = freq_i
                    freq_i = words[item]
                elif words[item] > freq_a and words[item] <= freq_i:
                    suspect_a = item
                    freq_a = words[item]
                #pepe
            elif len(item) == 3:
                if words[item] > freq_the:
                    suspect_the = item
                    freq_the = words[item]
        print(suspect_the, freq_the, ": suspected the")
        print(suspect_a, freq_a, ": suspected a")
        print(suspect_i, freq_i, ": suspected i")
        key[suspect_a] = "a"
        key["a"] = suspect_a
        key[suspect_the[0]] = "t"
        key["t"] = suspect_the[0]
        key[suspect_the[1]] = "h"
        key["h"] = suspect_the[1]
        key[suspect_the[2]] = "e"
        key["e"] = suspect_the[2]
        return key



def substitution(cipher):
    again = True
    type = input("words or letters ")
    while again:
        key = findKey(cipher,type)
        print("KEY: ",key)
        originalDiff = dictionary(cipher)
        for char in range(len(cipher)):
            if cipher[char] != " ":
                i = cipher[char]
                cipher[char] = key[i]

        print(dictionary(cipher),"from",originalDiff)
        print(arrayToString(cipher))
        y = input("again? ")
        if y == "n":
            again = False
        elif y == "s":
            if type == "w":
                type = "l"
            else:
                type = "w"







def ceasar(cipher):
    diffs = []
    for shift in range(26):
        for i in range(len(cipher)):
            if cipher[i] != " ":
                ascii = ord(cipher[i])
                if ascii+1 >= 123:
                    ascii = 96
                cipher[i] = chr(ascii+1)
        print(arrayToString(array),dictionary(array),shift,"\n")
        shifted = []
        for j in range(len(cipher)):
            shifted.append(cipher[j])
        diffs.append([shifted,dictionary(cipher),shift])
    pointer = 0
    for j in range(len(diffs)):
        if diffs[j][1] > diffs[pointer][1]:
            pointer = j
    diffs[pointer][0] = arrayToString(diffs[pointer][0])
    print(diffs[pointer])
    return diffs[pointer]










a = "GUR ANGVBANY NEPUVIRF VA XRJ PBAGNVA N GUBHFNAQ LRNEF BS UVFGBEL. QBPHZRAGF BS FGNGR QNGVAT ONPX BIRE N GUBHFNAQ LRNEF NER PNERSHYYL CERFREIRQ NAQ FGHQVRQ OL UVFGBEVNAF SEBZ NEBHAQ GUR JBEYQ – SVYRF GUNG NER BSGRA FRAFVGVIR NAQ ZNEXRQ JVGU N ERYRNFR QNGR JUVPU PBHYQ OR NF YBAT NF BAR UHAQERQ LRNEF SBE CNEGVPHYNEYL FRAFVGVIR VASBEZNGVBA. ZHPU YRFF JRYY XABJA VF GUR FUNQBJ NEPUVIR, QRRC VAFVQR GUR UBZR BS OEVGVFU PBQROERNXVAT JUVPU PBAGNVAF SVYRF GUNG ZVTUG ARIRE OR ERYRNFRQ. GURL PNEEL GUR ZNEX QGN, JUVPU QRABGRF QRYRTNGR GB NEPUNRBYBTL, GUR GRNZ ERFCBAFVOYR SBE GURZ OHG GUR NEPUVIVFGF WBXR GUNG VG FGBBQ SBE QBA\’G GRYY NALBAR. GURFR SVYRF PBAGNVA FRPERGF GUNG, NYBAT JVGU GURVE PVCURE XRLF, JRER YBFG YBAT NTB. AB-BAR XABJF JUNG GERNFHERF GURL ZVTUG PBAGNVA. VG VF LBHE WBO GB OERNX GUR PVCUREF NAQ GB SVAQ BHG!"
b = "EDCT OEEW VAKUE DZK U OUXX BAHJ JOA ZEO KACLYEZJH NAG QAL JA KECUBTEG. JTEQ DGE JDWEZ NGAY JTE DGCTUMEH TEGE DJ IAHH CEZJGDX DZK GEXDJE JA EMEZJH ACCLGGUZS AMEG AZE TLZKGEK DZK NUNJQ QEDGH DSA. U TDME D NEEXUZS JTDJ JTEQ YUSTJ HJUXX IE GEXEMDZJ!!! QALG JDHW UH JA KECGQBJ EDCT AN JTE KACLYEZJH DZK LBXADK QALG HAXLJUAZH AZ JTE CTDXXEZSE BDSEH. UN QAL YDWE D YUHJDWE QAL OUXX SEJ HAYE NEEKIDCW DZK CDZ JGQ DSDUZ. QAL OUXX SEJ D HCAGE NAG EDCT DJJEYBJ DZK OE OUXX ILUXK D XEDKEGIADGK LHUZS JTAHE HCAGEH. UN QAL DGE UZ D JEDY, JTEZ AZXQ JTE JEDY CDBJDUZ CDZ LBXADK HLIYUHHUAZH, HA YDWE HLGE QAL OAGW OUJT JTEY JA SEJ QALG DZHOEGH HLIYUJJEK. UZ QALG DCCALZJ BDSEH QAL OUXX NUZK D GECAGK AN QALG HLIYUHHUAZH, JASEJTEG OUJT D CABQ AN D CEGJUNUCDJE GECAGKUZS QALG BGASGEHH. UN QAL ODZJ QAL CDZ DXXAO QALG JEDCTEG JA NAXXAO QALG BGASGEHH IQ SEJJUZS JTE JEDY CDBJDUZ JA EZJEG D HBECUDX BUZ ZLYIEG (JTE JEDCTEG\’H YAZUJAGUZS BUZ) UZJA JTE JEDY KEJDUXH AZ JTEUG DCCALZJ BDSE. UN QAL TDME DZQ FLEHJUAZH JTEZ TEDK AMEG JA JTE NAGLY OTEGE QAL OUXX NUZK XAJH AN NGUEZKXQ DKMUCE! SAAK XLCW, TDGGQ"
oneA = "HT YZVMZNO ZGGZI, RZ VMZ, VO GVNO, VMMDQZY DI IZR TJMF, VIY D XVIIJO OZGG TJP CJR CVKKT D VH OJ WZ CZMZ. VAOZM V GJIB VIY VMYPJPN NZV EJPMIZT D XVIIJO NVT DO DN OCZ WZNO JA ODHZN, WPO DO DN AVM AMJH OCZ RJMNO! OCVIF TJP NJ HPXC AJM XJHHZIYDIB HZ OJ TJPM AMDZIY HM YDXFZIN. CZ DN V YZHVIYDIB ZHKGJTZM, WPO IJO PIFDIY, VIY OCZ RJMF DN ZIBVBDIB VIY MZRVMYDIB DI ZLPVG HZVNPMZ. ZIXJPMVBZY WT CDN BJJY AMDZIY HM RDGFDZ, CZ CVN WZBPI OJ XJINDYZM V IZR IJQZG DI OCZ NOTGZ JA V HTNOZMT, VIY D OCDIF DO HDBCO WZ CDN ADIZNO DYZV TZO. D VH IJO XZMOVDI RCZOCZM OCZ QJTVBZ DONZGA CVN ODMZY CDH, WPO CZ CVN NZZHZY DI GJR NKDMDON NDIXZ RZ VMMDQZY, VIY D VH CJKDIB OCVO OCDN IZR KMJEZXO RDGG CZGK OJ GDAO OCZH. D RJIYZM DA CDN YZHZVIJPM DN DI KVMO MZGVOZY OJ OCZ VKKZVMVIXZ JA V MVOCZM NOMVIBZ IJOZ OCVO RVN YZGDQZMZY OJ CDN XVWDI JI VMMDQVG DI OCZ KJMO. DO DN HJNO DIOMDBPDIB. VN TJP FIJR, D VH MZLPDMZY OJ JKZI VIY NJMO VGG OCZ HVDG, YZOZMHDIDIB RCDXC GZOOZMN, DA VIT, MZLPDMZ HM YDXFZIN VOOZIODJI. OCZ GZOOZM RVN HVMFZY \”NOMDXOGT KMDQVOZ AJM HM XCVMGZN YDXFZIN”, WPO D XJIAZNN D CVY VGMZVYT JKZIZY OCZ ZIQZGJKZ WZAJMZ D IJODXZY OCZ NOZMI DIEPIXODJI VIY OCZMZAJMZ CVY NZZI OCZ XJIOZION RCDXC RZMZ IJO AJM HT ZTZN. D NVT NZZI MVOCZM OCVI MZVY, AJM DO RVN DHKJNNDWGZ OJ MZVY OCZ RJMYN OCZMZDI, DA DIYZZY OCZT RZMZ RJMYN! OCZ XCVMVXOZMN, RCDGZ AVHDGDVM, HVYZ IJ NZINZ VIY D YZOZMHDIZY OJ MZKGVXZ OCZ GZOOZM DI DON ZIQZGJKZ VIY OJ KVNN DO OJ HM YDXFZIN RDOC HT VKJGJBDZN. CZ OJJF DO, NVTDIB IJOCDIB VIY NKZIO NJHZ ODHZ VGJIZ DI CDN XVWDI. D YDY IJO NZZ OCZ GZOOZM VBVDI WPO YDY YDNXJQZM V NHVGG KDGZ JA VNC DI V YDNC PKJI CDN YZNF. PIVWGZ OJ NPKKMZNN HT XPMDJNDOT D ZILPDMZY JA OCZ NCDK\’N NOZRVMY DA CZ FIZR VITOCDIB JA OCDN IJOZ, VIY CZ OJGY HZ OCVO DO CVY WZZI YZGDQZMZY WT CVIY, WT V HVI FIJRI OJ OCZ XMZR VN NZXMZOVMT OJ HM BMZIQDGGZ H. YJYBZ. D FIJR IJOCDIB JA OCDN HVI, WZTJIY OCZ AVXO OCVO CZ DN V RZVGOCT DIYPNOMDVGDNO, VIY D XVI JIGT NPKKJNZ OCVO CZ DN CJKDIB OJ HZZO OCZ AVHJPN VPOCJM KMDQVOZGT. DA NJ, D OCDIF CZ HVT WZ YDNVKKJDIOZY. JPM NXCZYPGZ DN VGMZVYT APGG, VIY D XVIIJO OCDIF OCVO RZ NCJPGY QVMT DO DI MZNKJINZ OJ OCZ HVIT NPXC MZLPZNON. NODGG, D XVIIJO ZNXVKZ OCZ DHKMZNNDJI OCVO OCDN RVN HJMZ OCVI V KMDQVOZ DIQDOVODJI. DA DO RZMZ OCZI D XVIIJO NZZ RCT DON XJIOZION RJPGY IZZY OJ WZ NZXPMZY. DO NZZHN OCZMZ HVT WZ HJMZ OCVI JIZ HTNOZMT VO CVIY. TJPMN NDIXZMZGT, XGVMV"
oneB = "FRWXT KFKWB VDXGL BMKNL MMATM RHNKC HNKGX RPTLN GXOXG MYNET GWAHI XRHNP BEEGH MFBGW FRWBK XVMGX LLBGP KBMBG ZMHRH NHGRH NKTKK BOTEB GGXPR HKDBT IIKXV BTMXM ATMRH NFTRG XXWTE BMMEX MBFXM HLXMR HNKHP GIETG LBGFH MBHGU NMMAB GZLTK XFHOB GZLHF XPATM YTLMX KMATG BXGOB LTZXW PAXGB YBKLM TIIKH TVAXW FKUTU UTZXP BMAFR IKHIH LTEBY XTKMA TMBGM AXLXW TGZXK HNLMB FXLBM BLGXV XLLTK RMHKX TVMMH XOXGM LPBMA LIXXW BYPXT KXMHA TOXTG RAHIX HYLAT IBGZH NKWXL MBGRP BMAEN VDBMB LGHMM HHETM XMHXF UTKDH GHNKO XGMNK XBNGW XKLMT GWMAT MRHNK LVAXW NEXBL GHMRX MYBGT EBLXW LHVTG BBFIE HKXRH NMHVH GLBWX KFHOB GZYHK PTKWR HNKOB LBMMH PTLAB GZMHG MAXKX TKXIX HIEXA XKXHY VHGLX JNXGV XPAHT KXXTZ XKMHF XXMPB MARHN TGWPA HFBZA MUXIX KLNTW XWURR HNMHC HBGPB MANLB YMAXL TVKBY BVXHY LHFTG RZHHW FXGTG WPHFX GBLGH MMHUX PTLMX WMAXG PXPBE EGXXW MAXBK LNIIH KMRHN ATOXT EKXTW RLAHP GTKXF TKDTU EXLDB EEBGX QIHLB GZBGC NLMBV XTGWI XKLNT WBGZM AXPXT EMARM HPHKD PBMAR HNMHT WWKXL LBMHG RHNKL BWXHY MAXTM ETGMB VAXKX BGMAX NGBMX WLMTM XLPXT KXWXL IXKTM XERBG GXXWH YRHNK TWOHV TVRBY PXTKX MHVHG LHEBW TMXMA XZTBG LPHGB GHNKF HLMNG VBOBE PTKPB MAFRO XKRUX LMPBL AXLZK XGOBE EXFWH WZX"
twoA = "PZ ORFE XERSQDMMR, D PNHK FYVMVXDHR UVE LAFEMRH, AR DH F XVVO PFS, INK LFS IR DEFHLDIMR, FSO KEFQRM ERFMMZ OVRH SVK HNDK ADP. D ERFO ADH MRKKRE KV ZVN TDKA HVPR LVSLRES (KAFSJ ZVN UVE HRSODSX PR F LVYZ), HRRDSX KAFK DK ORPVSHKEFKRH F MVTSRHH DS ADH HYDEKH, INK D LFS FHHNER ZVN KAFK AR DSKRSOH VSMZ KAR IRHK UVE VNE RSORFQVNE. DK KVVJ KAR LVPIDSRO RUUVEKH VU PZHRMU FSO MVEO OREIZ KV LVSQDSLR ADP VU KAR EDXAKSRHH VU VNE YMFS, INK TADMR AR DH UNMMZ LVPPDKKRO KV VNE LFNHR, AR DH SVK RSKDERMZ FK RFHR TDKA VNE PRKAVOH. D AFQR LVSKDSNRO KV HVMDLDK HNYYVEK UVE ZVNE YEVYVHFM VS KADH HDOR VU KAR FKMFSKDL, FSO D FP LVSUDORSK KAFK PZ VTS HPFMM LVSKEDINKDVS LFS YMFZ FS DPYVEKFSK YFEK DS DKH HNLLRHH. D KENHK KAFK ZVNE XEVNY ERPFDSH LVSUDORSK KAFK DK LFS ORMDQRE VS DKH YEVPDHR. TDKA KAR HNYYVEK VU KAR IEDKDHA FSO FPREDLFS XVQRESPRSKH D KADSJ TR LVNMO INDMO HVPRKADSX RSKDERMZ SRT FSO RWKERPRMZ YVTREUNM, AVTRQRE KAR KENR YVKRSKDFM LFS VSMZ IR PRK DU TR LFS RSHNER KVKFM HRLERLZ, FSO D TDMM AFQR KV ERMZ VS ZVN KV YREHNFOR LAFEMRH SVK KV HYRFJ VU VNE ORHDXSH TDKA FSZVSR VNKHDOR VU VNE LDELMR. UVE ADH VTS YFEK, LAFEMRH DH LADRUMZ DSKRERHKRO DS KAR HNLLRHH VU ADH KVNE, FSO TADMR AR TDMM YMFZ FS DPYVEKFSK EVMR DS YREHNFODSX DSQRHKVEH KV GVDS VNE HLARPR FSO YVMDKDLDFSH KV HNYYVEK DK, DK DH DPYVEKFSK KAFK AR DH FMHV FIMR KV RSGVZ KAR UENDKH VU ADH ERFODSX YREUVEPFSLRH. AR DSQRHKH PNLA VU ADPHRMU DS KAVHR ERFODSXH FSO DH DSLMDSRO KV VQREKDER ADPHRMU. D KENHK KAFK ZVN FSO ZVNE UEDRSOH TDMM VUURE ADP KAR HNYYVEK KAFK D TVNMO VUURE DU D LVNMO IR KARER TDKA ADP. TDKAVNK KAFK HNYYVEK D URFE KAFK AR TDMM AFQR SV RSREXZ MRUK KV YEVPVKR VNE YEVGRLK. ZVNE UEDRSO, LAFEMRH IFIIFXR"
twoB = "GRV XKF TXXFQXLRQ RG JFQFVTO EREJF PV EREJF, AKLOF L ITQQRX IOTLP XR KTZF VFIRZFVFE GYOOC GVRP XKF VLJRYVW RG PC MRYVQFC, L KTZF QRA TEMYWXFE XR CRYV IOLPTXF TQE KTZF HFJYQ XR FWXTHOLWK PC VRYXLQF. L KRSF CRY ALOO QRX XTNF LX HTEOC XKTX L TP VFOYIXTQX XR TJVFF XR CRYV VFUYFWX XR FBSFELXF PC ZLWLX XR ATWKLQJXRQ, HYX L TP QR ORQJFV T CRYQJ PTQ, TQE PC SFVGRVPTQIFW VFUYLVF IRQWLEFVTHOF FQFVJC GVRP PF. TJF LW XKF XKLFG RG XLPF, TQE QRQF RG YW NQRA KRA UYLINOC LX LW WXROFQ GVRP YW. L PYWX ER AKTX L ITQ XR PTVXLTO XKTX PRWX SVFILRYW VFWRYVIF. RYV PYXYTO GVLFQE, PV HTHHTJF, KTW IRPPFQEFE CRY XR PF, TQE RYV RAQ SVLPF PLQLWXFV KTW XTNFQ STLQW XR FBSOTLQ XR PF XKF LPSRVXTQIF RG CRYV PLWWLRQ, KRAFZFV L GTLO XR WFF KRA VFTVVTQJLQJ PC WIKFEYOF ALOO ER TQCXKLQJ PYIK XR WSFFE XKF SVRJVFWW RG AKTX PYWX QFIFWWTVLOC HF T ORQJ-XFVP LQZFWXPFQX RG ITSLXTO TQE VFWRYVIFW. L KTZF SVRPLWFE XKTX L ALOO ER AKTX L ITQ XR TWWLWX CRY, HYX L PYWX IRQWLEFV PC RAQ KFTOXK TQE AFOGTVF LG L TP XR IRPSOFXF XKLW XRYV. PTC L TOWR VFPTVN XKTX LG XKF ARVN RQ AKLIK CRY TVF FPHTVNFE LW XVYOC TW WFIVFX TW CRY TQE HTHHTJF WFFP XR HFOLFZF, XKFQ XKF YWF RG TQILFQX ILSKFVW ERFW QRX PFFX XKTX QFFE. L KTZF XTNFQ XKF OLHFVXC RG YWLQJ WRPFXKLQJ T OLXXOF PRVF TSSVRSVLTXF LQ XKLW OFXXFV TQE ARYOE WYJJFWX XKTX SFVKTSW AF YWF XKLW PFXKRE GRV RYV GYXYVF IRPPYQLITXLRQW. CRYVW WLQIFVFOC, IKTVOFW ELINFQW"
a = setUp(a)
b = setUp(b)
oneA = setUp(oneA)
oneB = setUp(oneB)
twoA = setUp(twoA)
twoB = setUp(twoB)


#ceasar(oneA)
ceasar(twoA)

#ceasar(a)
# substitution(b)

