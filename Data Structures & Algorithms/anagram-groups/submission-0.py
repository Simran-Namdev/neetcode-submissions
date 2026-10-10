class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            keymap = [0] * 26

            for char in s:
                keymap[ord(char) - ord('a')] += 1

            key = tuple(keymap)
            hashmap.setdefault(key, []).append(s)

        return list(hashmap.values())


        