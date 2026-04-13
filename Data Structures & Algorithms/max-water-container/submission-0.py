class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            area = min(heights[l], heights[r]) * (r - l) #basically min height into the width (the distance between the nodes)
            if area > res:
                res = area
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res