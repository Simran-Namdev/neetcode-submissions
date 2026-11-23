class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(n, i):
            # if n not in res:
            
            if i == len(nums):
                res.append(n.copy())
                return
            
            
            n.append(nums[i])
            backtrack(n, i + 1)
            n.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(n, i + 1)
        
        backtrack([], 0)
        return res
        