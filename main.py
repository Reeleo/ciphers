import ciphers
import solve
import freq
 



sixAKey2 = {"a":"d", "b":"n", "c":"a", "d":"u", "e":"w", "f":"k", "g":"s",
        "h":"p", "i":"h", "j":"t", "k":"m", "l":"e", "m":"b", "n":"v",
        "o":"j", "p":"f", "q":"x", "r":"g", "s":"y", "t":"r", "u":"o",
        "v":"q", "w":"z", "x":"l", "y":"c", "z":"i"} 

sixAKey2 = {"a":"c", "b":"o", "c":"a", "d":"p", "e":"f", "f":"f", "g":"r",
        "h":"b", "i":"s", "j":"t", "k":"u", "l":"e", "m":"v", "n":"w",
        "o":"d", "p":"y", "q":"q", "r":"d", "s":"g", "t":"h", "u":"i",
        "v":"v", "w":"k", "x":"l", "y":"m", "z":"n"} 


sixAKey1 = [0,3,2,1]



sixA = solve.sSubstitution(ciphers.sixA,sixAKey2)
print(solve.transposition(sixA,sixAKey1))


print(sorted(freq.FREQ.items(), key=lambda x:x[1], reverse=True))



