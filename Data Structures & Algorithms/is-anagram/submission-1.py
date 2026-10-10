class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {i:0 for i in range(26)}
        tmap = {i:0 for i in range(26)}

        for idx in range(len(s)):
            i = s[idx]
            smap[ord(i) - ord('a')] += 1

        for idx in range(len(t)):
            j = t[idx]
            tmap[ord(j) - ord('a')] += 1
        
        for i, j in zip(smap.values(), tmap.values()):
            if i != j:
                return False
        return True

        