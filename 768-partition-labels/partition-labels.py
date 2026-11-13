class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last={}
        for i in range(len(s)):
            last[s[i]]=i
        start=0
        end=0
        result=[]
        for i in range(len(s)):
            end=max(end,last[s[i]])
            if i==end:
                result.append(end-start+1)
                start=i+1
        return result