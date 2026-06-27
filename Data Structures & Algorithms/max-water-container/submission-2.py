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
            elif heights[l]>heights[r]:
                r=r-1
            elif heights[l]==heights[r]:
            # move the pointer which is leading to bigger volume
            #no need to multiply by r-l since it is gonna be same each side
                if (l<r) and (heights[l+1]*heights[r] > heights[l]*heights[r-1]):
                    l=l+1
                elif (l<r) and (heights[l+1]*heights[r] < heights[l]*heights[r-1]):
                    r=r-1
                elif (l<r) and (heights[l+1]*heights[r] == heights[l]*heights[r-1]):
                    r=r-1
                    l=l+1
        return max_vol
                