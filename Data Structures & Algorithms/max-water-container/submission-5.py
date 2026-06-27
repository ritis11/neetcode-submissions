class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_vol = 0
        while l<r:
            volume = min(heights[l], heights[r]) * (r-l)
            if volume > max_vol:
                max_vol=volume
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1

        return max_vol
                