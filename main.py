def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t)
        return False

    countS, countT = {}, {}

    # building the hashmap
    for i in range(len(s)):
        # increment the count of a character by 1 everytime it appears
        # get() to get the key of the letter in the hashmap, zero is the default value
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True

