class Solution:
    def totalMoney(self, n: int) -> int:
        total=0
        monday=1
        for day in range(n):
            total=total+monday+day%7
            if day%7==6:
                monday+=1
        return total