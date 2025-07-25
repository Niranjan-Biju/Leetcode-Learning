'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        sorted_arr = sorted(merged)
        num = len(sorted_arr)
        middle_element = num//2
        median = 0

        if num%2==0:
            median = (sorted_arr[middle_element] + sorted_arr[middle_element - 1]) / 2
        else:
            median = sorted_arr[middle_element]

        return median

# Binary Search Solution 
class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2      
            j = half - i               

           
            left1 = float('-inf') if i == 0 else nums1[i - 1]
            right1 = float('inf') if i == m else nums1[i]
            left2 = float('-inf') if j == 0 else nums2[j - 1]
            right2 = float('inf') if j == n else nums2[j]

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    return max(left1, left2)
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1
