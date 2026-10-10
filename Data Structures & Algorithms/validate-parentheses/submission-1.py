class Solution:
    def isValid(self, s: str) -> bool:
        brack = {'(':')', '{':'}', '[':']'}
        

        stack = []

        for b in s:
            if b in brack:
                stack.append(b)
            else:
                if not stack:
                    return False
                l = stack.pop()
                if b != brack[l]:
                    return False
        return not stack
        
        