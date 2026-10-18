class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=dict()
        for i, ele in enumerate(nums):
            if target-ele in seen:
                return sorted([i, seen[target-ele]])
            seen[ele]=i