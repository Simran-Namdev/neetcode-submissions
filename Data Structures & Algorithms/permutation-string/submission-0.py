class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map= {}
        s2map= {}
        for c in s1:
            s1map[c] = s1map.get(c, 0) + 1

        l = 0
        for r, c in enumerate(s2):
            if (r - l + 1) > len(s1):
                s2map[s2[l]] -= 1
                if s2map[s2[l]] == 0:
                    del s2map[s2[l]]
                l += 1
            s2map[c] = s2map.get(c, 0) + 1

            if s1map == s2map:
                return True
        return False
            

        