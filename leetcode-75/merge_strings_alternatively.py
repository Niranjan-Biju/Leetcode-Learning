'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        len1=len(word1)
        len2=len(word2)
        result=[]
        while i<len1 and i<len2:
            result.append(word1[i])
            result.append(word2[i])
            i+=1      
        if i<len1:
            result.extend(word1[i:])
        elif i<len2:
            result.extend(word2[i:])

        return ''.join(result)
