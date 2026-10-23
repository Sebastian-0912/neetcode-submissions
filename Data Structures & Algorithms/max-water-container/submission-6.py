class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right=0, len(heights)-1
        ans = (right-left)*min(heights[left], heights[right])
        while left<right:
            if heights[left]<= heights[right]:
                next_high=left
                while next_high < right:
                    if heights[next_high]<= heights[left]:
                        next_high+=1
                    else:
                        break
                left=next_high
                new_area=(right-left)*min(heights[left], heights[right])
                ans = max(ans, new_area)
            else:
                next_high=right
                while next_high > left:
                    if heights[next_high]<= heights[right]:
                        next_high-=1
                    else:
                        break
                right=next_high
                new_area=(right-left)*min(heights[left], heights[right])
                ans = max(ans, new_area)
        return ans