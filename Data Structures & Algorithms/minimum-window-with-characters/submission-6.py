class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        need=Counter(t)
        missing=len(t)
        best_len = float("inf")
        best_left=0
        for right, char in enumerate(s):
            if char in need:
                if need[char]>0:
                    missing-=1
                need[char]-=1
            while missing==0:
                window_len = right-left+1
                if window_len < best_len:
                    best_left = left
                    best_len = window_len
                outgoing=s[left]
                if outgoing in need:
                    need[outgoing]+=1
                    if need[outgoing]>0:
                        missing+=1
                left+=1
        if best_len == float("inf"):
            return ""
        return s[best_left:best_left+best_len]