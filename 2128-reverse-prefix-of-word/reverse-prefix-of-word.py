class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        char=list(word)
        right=word.find(ch)
        left=0
        while left<right:
            char[left],char[right]=char[right],char[left]
            left+=1
            right-=1
        return "".join(char)