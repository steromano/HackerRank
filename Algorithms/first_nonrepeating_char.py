with open("input003.txt") as f:
    s = f.read()

def firstNonRepeatingCharacter(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c in s:
        if counts[c] == 1:
            return c
    return None

print firstNonRepeatingCharacter(s)