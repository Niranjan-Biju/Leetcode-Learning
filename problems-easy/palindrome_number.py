'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

# Solution 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        sum_val=0
        num = x
        
        while num>0:
            digit = num%10
            sum_val = sum_val*10 + digit
            num//=10
        
        return sum_val==x
