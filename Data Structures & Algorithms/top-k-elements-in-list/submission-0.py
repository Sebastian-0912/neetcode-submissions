class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk =[key for key,time in Counter(nums).most_common(k)]
        return topk