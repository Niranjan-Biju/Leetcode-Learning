'''
Convert Roman numerals to its integer counterpart.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        total=0
        prev_value=0
        for roman_num in reversed(s):
            curr_value=roman[roman_num]

            if curr_value<prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value=curr_value

        return total

