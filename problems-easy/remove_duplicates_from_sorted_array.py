'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0 # for counting and points to most recent unique value
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1

'''
What this code does-
  A pointer i points to the first element. This pointer points to the latest unique element. Another pointer j checks every element starting from 2nd element against the element at i. If the element at j and 
  element at i is not same (a new number has been found), i is incremented by i and the element at i is changed to element at j. This ensures i currently points to the latest element. Since i starts at 0, 
  the total number of elements that are unique is i+1.
'''
  
