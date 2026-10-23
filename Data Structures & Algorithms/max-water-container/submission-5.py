class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right=0, len(heights)-1
        ans = (right-left)*min(heights[left], heights[right])
        while left<right:
            new_area=(right-left)*min(heights[left], heights[right])
            ans = max(ans, new_area)
            if heights[left]<= heights[right]:
                left+=1
            else:
                right-=1
        return ans