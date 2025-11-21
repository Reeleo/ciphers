import ciphers
import solve
import freq
 



sixBkey = "newyork"

print(solve.vigenere(ciphers.sixB,sixBkey))


print(sorted(freq.FREQ.items(), key=lambda x:x[1], reverse=True))



