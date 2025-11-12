import ciphers
import solve
import freq
 
fourBkey = {"a":"a", "b":"y", "c":"c", "d":"a", "e":"d", "f":"e", "g":"c",
        "h":"f", "i":"g", "j":"h", "k":"i", "l":"j", "m":"k", "n":"l",
        "o":"b", "p":"m", "q":"n", "r":"o", "s":"p", "t":"y", "u":"r",
        "v":"s", "w":"t", "x":"u", "y":"v", "z":"w"} 





print(ciphers.fourB)
print(solve.substitution(ciphers.fourB,fourBkey))

#solve.substitution(ciphers.twoB,twoBkey)






