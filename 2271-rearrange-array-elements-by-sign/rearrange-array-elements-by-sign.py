class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos=0
        neg=1
        result=[0]*len(nums)
        for num in nums:
            if num>0:
                result[pos]=num
                pos+=2
            else:
                result[neg]=num
                neg+=2
        return result