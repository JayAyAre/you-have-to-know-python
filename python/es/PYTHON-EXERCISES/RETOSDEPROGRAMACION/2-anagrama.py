"""
MEDIO

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando TODAS
        las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word1, word2):
    if word1 == word2:
        return False
    else:
        word1 = word1.lower()
        word2 = word2.lower()
        if len(word1) != len(word2):
            return False
        else:
            word1 = list(word1)
            word2 = list(word2)
            word1.sort()
            word2.sort()
            if word1 == word2:
                return True
            else:
                return False

print(is_anagram("ana", "lan"))
print(is_anagram("lan", "ana"))
print(is_anagram("ana", "ana"))
print(is_anagram("lan", "lan"))

print(is_anagram("iman", "mani"))