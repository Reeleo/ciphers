import ciphers
import solve
import freq
 

#[10, 23, 23, 26, 26, 24, 23]
sevenBkey = "zkjniu" # mydear
sevenBkey = "zkjniumkt" # mydearest
sevenBkey = "iemaetx" # dearest
sevenBkey = "zr" # mr

sevenBkey = "friend"

'''
NAMES
clara
ellen
charles babbage
charles dickens
general grenville m dodge
rokesmith
molin
lord derby
frederick douglass
thaddeus
charles

senator grimes
mr johnson
'''

# need to look at playfair cipher


print("start")
#print(solve.vigFreq(ciphers.sevenB,5))
print(solve.vigenere(ciphers.sevenB,sevenBkey))


#print(sorted(freq.FREQ.items(), key=lambda x:x[1], reverse=True))



