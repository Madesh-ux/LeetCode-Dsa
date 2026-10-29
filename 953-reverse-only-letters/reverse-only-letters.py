class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans=list(s)
        i=0
        j=len(ans)-1
        while i<j:
            if not ans[i].isalpha():
                i+=1
            elif not ans[j].isalpha():
                j-=1
            else:
                ans[i],ans[j]=ans[j],ans[i]
                i+=1
                j-=1
        return "".join(ans)