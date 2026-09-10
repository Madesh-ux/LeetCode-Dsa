class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = len(nums)-1
        start = final - 1

        while start >= 0:
            if nums[start] + start >= final:
                final = start
            start -= 1
        if final == 0:
            return True
        else:
            return False