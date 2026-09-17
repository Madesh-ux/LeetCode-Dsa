class Solution:
    def maxArea(self, height: list[int]) -> int:
        res=0
        left=0
        right=len(height)-1
        while left<right:
            area=(right-left)*min(height[left],height[right])
            res=max(res,area)
            if height[left]<height[right]:
                left+=1
            #elif height[right]<height[left]:
                #right+=1
            else:
                right-=1 #This also solves height[left]==height[right] and height[right]<height[left]
        return res