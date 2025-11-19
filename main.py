import ciphers
import solve
import freq
 



# #mydear
# fiveBkey = "qnvqao"

# #dearest
# fiveBkey = "htsdape"


#print(freq.freqLetters(ciphers.fiveB))
#print(solve.sSubstitution(ciphers.fiveB,fiveBkey))


print(sorted(freq.FREQ.items(), key=lambda x:x[1], reverse=True))



