class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(n, i):
            nonlocal res
            if n not in res:
                res.append(n.copy())
            if i >= len(nums):
                return
        
            backtrack(n, i + 1)
            n.append(nums[i])
            backtrack(n, i + 1)
            n.pop()
            
        for i in range(len(nums)):
            backtrack([], i)
        return res

