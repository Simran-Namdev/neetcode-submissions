class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(n, i, s):
            if i >= len(nums):
                return
            if s > target:
                return
            if s == target and n not in res:
                res.append(n.copy())
                return

            # backtrack(n, i, s)
            backtrack(n, i + 1, s)
            s += nums[i]
            n.append(nums[i])
            backtrack(n, i, s)
            # backtrack(n, i + 1, s)
            n.pop()
            
        
        backtrack([], 0, 0)
        return res
        
            


        