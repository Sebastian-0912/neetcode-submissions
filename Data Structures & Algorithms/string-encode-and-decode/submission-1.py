class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#"+word for word in strs)

    def decode(self, s: str) -> List[str]:
        # 6#Hell#o5#world
        ans=[]
        i=0
        while i<len(s):
        # find valid #
            j=s.find("#",i)
        # see word length
            # length=int(s[j-1]) # wrong
            length=int(s[i:j])
        # read real word and push to ans array
            word=s[j+1:j+1+length]
            ans.append(word)
        # move i to next start point
            i = j+length+1
        return ans