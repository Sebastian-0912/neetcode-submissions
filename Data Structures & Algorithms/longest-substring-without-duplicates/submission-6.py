class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        left=0
        last_seen={}
        for right, char in enumerate(s):
            if char in last_seen:
                if left < last_seen[char]+1 :
                    left = last_seen[char]+1
            last_seen[char]=right
            longest = max(longest, right-left+1)
        return longest