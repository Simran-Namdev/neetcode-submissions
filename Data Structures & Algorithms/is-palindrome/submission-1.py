class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = "".join(i.lower() for i in s if i.isalnum())

        i, j = 0, len(strs) - 1

        while i < j:
            if strs[i] != strs[j]:
                return False
            i += 1
            j -= 1
        return True
        

        