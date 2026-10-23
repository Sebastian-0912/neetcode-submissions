class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0
        left=0
        freq=dict.fromkeys(s,0)
        # print(freq)
        for right, char in enumerate(s):
            freq[char]+= 1
            while (right-left+1) - max(freq.values()) > k:
                freq[s[left]]-=1
                left+=1
            longest=max(right-left+1, longest)
        return longest
