class Solution:
    def maxArea(self, height: List[int]) -> int:
        #create two pointer
        l, r = 0, len(height) - 1
        #create a variable to store the current max water = (r - l) * min(height[l], height[r]
        max_area = 0
        #find the smaller height and shift the according pointer
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] <= height[r]: l += 1
            elif height[l] > height[r]: r -= 1

        return max_area