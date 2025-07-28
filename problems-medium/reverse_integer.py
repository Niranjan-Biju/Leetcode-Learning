'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        rev_num=0
        if x<0:
            x = -x
            sign = -1
        while x>0:
            rev_num = rev_num*10+(x%10)
            x//=10        
            
        if rev_num.bit_length() >= 32:
            return 0
        return rev_num*sign
