# Task: https://py.checkio.org/en/mission/count-morse/

from itertools import permutations

res = 0

D = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}

def count_morse_(message: str, letters: str, index, morse_string) -> int:
    msg = message
    ok = True
    for ch in letters:
        if msg.startswith(D[ch])  and (ch not in morse_string):
            morse_string += ch
            if str(msg[len(D[ch]):]) == '':
                if all(ch in morse_string for ch in letters):
                    index+=1
                morse_string = str(morse_string[:-2])
                return (index, morse_string)
            (index, morse_string) = count_morse_(str(msg[len(D[ch]):]), letters, index, morse_string)
        else:
            ok = False
    morse_string = str(morse_string[:-1])
    if not ok: # no correct next chars
        return (index, morse_string)
    return (index, morse_string)

