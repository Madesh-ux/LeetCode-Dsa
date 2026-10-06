class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        res=0
        maxf=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            maxf=max(maxf,count[s[right]])
            window_size=right-left+1
            while window_size-maxf>k:
                count[s[left]]-=1
                left+=1
                window_size=right-left+1
            res=max(res,window_size)
        return res