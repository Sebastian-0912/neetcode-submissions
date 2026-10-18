class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsmap={}
        for i, ele in enumerate(strs):
            anagram=str(sorted(ele))
            if  anagramsmap.get(anagram,0):
                anagramsmap[anagram].append(i)
            else:
                anagramsmap[anagram]=[i]
        ans=[]
        for value in anagramsmap.values():
            anagrams=[strs[item] for item in value]
            ans.append(anagrams)
        return ans