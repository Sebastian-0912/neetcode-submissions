class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map={}
        for num in nums:
            if num not in counter_map:
                counter_map[num]=0
            counter_map[num]+=1
        freq_list = sorted(list(counter_map.items()), key=lambda x:x[1], reverse=True)
        order_freq = [num for num,_ in freq_list]
        return order_freq[:k]
