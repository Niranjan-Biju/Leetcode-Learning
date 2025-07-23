"""
Problem:

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
"""

class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos=0
        neg=0
        res=0
        for i in nums:
            if i!=0:
                if i>0:
                    pos+=1
                else:
                    neg+=1
        res = pos if pos>neg else neg
        return res
