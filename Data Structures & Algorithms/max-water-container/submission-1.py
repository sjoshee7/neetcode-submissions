class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container = 0
        temp = 0
        l = 0
        r = len(heights)-1
        
        while l < r:
            temp = min(heights[l], heights[r]) * (r - l)
            container = max(temp, container)
            if heights[l] < heights[r] and l < r:
                l += 1
            else:
                r -= 1

        return container
