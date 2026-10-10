class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in mapp:
                return [mapp[diff], i]
            
            mapp[j] = i 
           
        
        