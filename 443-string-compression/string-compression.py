class Solution:
    def compress(self, chars: list[str]) -> int:
        insert,i=0,0
        while i<len(chars):
            group=1
            while (group+i)<len(chars) and chars[i]==chars[group+i]:
                group+=1
            chars[insert]=chars[i]
            insert+=1
            if group>1:
                string=str(group)
                chars[insert:insert+len(string)]=list(string)
                insert+=len(string)
            i+=group
        return insert