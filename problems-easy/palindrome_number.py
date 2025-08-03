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

# Optimised
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (but not 0 itself) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # If the number is even-length, x should equal reversed_half
        # If the number is odd-length, x should equal reversed_half // 10 (middle digit doesn't matter)
        return x == reversed_half or x == reversed_half // 10
