'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        max_h=max(height)

        while left<right:
            h = min(height[left],height[right])
            l = right - left
            area = h*l            
            max_area = max(area,max_area)

            if max_area>max_h*l:
                break
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return max_area
                

