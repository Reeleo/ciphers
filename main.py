import ciphers
import solve
import freq
 


#[7, 21, 12, 25, 6, 11, 8]
#[19, 5, 14, 1, 20, 15, 18]
sevenAkey = "senator"

print(solve.vigFreq(ciphers.sevenA,7))
print(solve.vigenere(ciphers.sevenA,sevenAkey))


#print(sorted(freq.FREQ.items(), key=lambda x:x[1], reverse=True))



