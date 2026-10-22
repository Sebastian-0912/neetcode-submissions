class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        left, right = 0, 1
        length=0
        seen=set()
        seen.add(s[0])
        while right<len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
            else:
                seen.discard(s[left])
                left+=1
            length=max(length, right-left)
        return length