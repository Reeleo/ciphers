import ciphers
import solve
import freq
 

fiveBkey = {"a":"a", "b":"b", "c":"c", "d":"r", "e":"e", "f":"f", "g":"g",
        "h":"h", "i":"d", "j":"j", "k":"k", "l":"y", "m":"m", "n":"n",
        "o":"e", "p":"p", "q":"q", "r":"r", "s":"s", "t":"t", "u":"u",
        "v":"v", "w":"m", "x":"x", "y":"y", "z":"z"} 

fiveBkey = {"a":"a", "b":"b", "c":"c", "d":"d", "e":"e", "f":"f", "g":"g",
        "h":"h", "i":"i", "j":"j", "k":"k", "l":"l", "m":"m", "n":"n",
        "o":"o", "p":"p", "q":"q", "r":"r", "s":"s", "t":"t", "u":"u",
        "v":"v", "w":"w", "x":"x", "y":"y", "z":"z"} 

#mydear
fiveBkey = "qnvqao"

#dearest
fiveBkey = "htsdape"


#print(freq.freqLetters(ciphers.fiveB))
print(solve.vigenere(ciphers.fiveB,fiveBkey))





