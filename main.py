import ciphers
import solve
import freq
 

fiveBkey = {"a":"a", "b":"b", "c":"c", "d":"d", "e":"e", "f":"f", "g":"g",
        "h":"h", "i":"i", "j":"j", "k":"k", "l":"l", "m":"m", "n":"n",
        "o":"o", "p":"p", "q":"q", "r":"r", "s":"s", "t":"t", "u":"u",
        "v":"v", "w":"w", "x":"x", "y":"y", "z":"z"} 

fiveBkey = {"a":"a", "b":"j", "c":"p", "d":"i", "e":"n", "f":"t", "g":"l",
        "h":"b", "i":"h", "j":"c", "k":"x", "l":"m", "m":"q", "n":"v",
        "o":"e", "p":"w", "q":"r", "r":"r", "s":"z", "t":"f", "u":"k",
        "v":"d", "w":"g", "x":"s", "y":"o", "z":"y"} 

# #mydear
# fiveBkey = "qnvqao"

# #dearest
# fiveBkey = "htsdape"


#print(freq.freqLetters(ciphers.fiveB))
print(solve.sSubstitution(ciphers.fiveB,fiveBkey))


print(sorted(freq.FREQ.items(), key=lambda x:x[1], reverse=True))



