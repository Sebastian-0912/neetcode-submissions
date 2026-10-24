class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        need = Counter(t)
        missing = len(t)

        left = 0
        best_start = 0
        best_len = float("inf")

        for right, char in enumerate(s):
            # Expand the window
            if char in need:
                if need[char] > 0:
                    missing -= 1
                need[char] -= 1

            # Shrink while valid
            while missing == 0:
                window_len = right - left + 1

                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                # Remove left character
                outgoing = s[left]

                if outgoing in need:
                    need[outgoing] += 1

                    if need[outgoing] > 0:
                        missing += 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]