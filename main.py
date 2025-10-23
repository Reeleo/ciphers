import ciphers
import solve
 
threeAkey = {"a":"a", "b":"i", "c":"c", "d":"d", "e":"e", "f":"m", "g":"n",
           "h":"a", "i":"o", "j":"j", "k":"k", "l":"l", "m":"d", "n":"n",
           "o":"e", "p":"d", "q":"t", "r":"r", "s":"u", "t":"t", "u":"w",
           "v":"v", "w":"w", "x":"x", "y":"g", "z":"h"}

solve.substitution(ciphers.threeA,threeAkey)

#solve.substitution(ciphers.twoB,twoBkey)





