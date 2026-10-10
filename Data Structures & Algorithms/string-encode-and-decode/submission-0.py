class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lengths = "".join("?" + str(len(s)) for s in strs)
        return str(len(strs)) + "?" + "".join(strs) + lengths

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        i = s.index("?")
        count = int(s[:i])
        lengths = s.rsplit("?", count)[1:]  
        res, pos = [], i + 1
        for p in lengths:
            n = int(p)
            res.append(s[pos:pos + n])
            pos += n
        return res