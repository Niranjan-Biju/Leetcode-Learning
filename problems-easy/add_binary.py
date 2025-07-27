'''
Given two binary strings a and b, return their sum as a binary string.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2)
        y = int(b,2)
        # Convert to integer

        while y!=0:
            sum = x^y # sum without carry
            carry = (x&y)<<1 #find carry and shift left
            x=sum
            y=carry # carry to be added to sum
        return bin(x)[2:] # convert to string, remove '0b'
