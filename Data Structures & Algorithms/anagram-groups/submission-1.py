class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for i, word in enumerate(strs):
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key]=[word]
        ans = list(groups.values())
        return ans