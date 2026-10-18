class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums=sorted(set(nums))
        max_len=1 if len(nums)>0 else 0
        length=1
        for i in range(0,len(sorted_nums)-1):
            current=sorted_nums[i]
            if sorted_nums[i+1]-current==1 :
                length+=1
                if length>max_len:
                    max_len=length
            else:
                length=1
        return max_len
