class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        h={}
        for i,num in enumerate(nums):
            if num in h:
                if i-h[num]<=k:
                    return True
            h[num]=i
        return False