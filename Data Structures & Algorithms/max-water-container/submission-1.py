class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        water = 0

        while l < r:
            w = min(heights[r] , heights[l]) * (r - l)
            water = max(w, water)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return water

        
        