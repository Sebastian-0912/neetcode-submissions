class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest=0
        for num in nums:
            if num-1 not in seen:
                current=num
                length=0
                while current in seen:
                    length+=1
                    current+=1
                longest=max(length,longest)
        return longest

