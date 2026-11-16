class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        char=list(s)
        left=0
        right=k-1
        while left<right:
            char[left],char[right]=char[right],char[left]
            left+=1
            right-=1
        return "".join(char)