class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t ==  "":
            return ""
        smap = {}
        tmap = {}
        res = [-1, -1]
        reinf = float("infinity")
        have = 0
       
        for c in t:
            tmap[c]  = 1 + tmap.get(c, 0)
        need = len(tmap)
        l = 0
        for r in range(len(s)):
            smap[s[r]] = 1 + smap.get(s[r], 0)
            if s[r] in tmap and smap[s[r]] == tmap[s[r]]:
                have += 1
            while have == need:
                if reinf > (r - l + 1):
                    reinf = r - l + 1
                    res = [l, r]
                smap[s[l]] -= 1
                if s[l] in tmap and smap[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if reinf != float("infinity") else ""





        