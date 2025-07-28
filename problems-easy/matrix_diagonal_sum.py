'''
Given a square matrix mat, return the sum of the matrix diagonals - both left diagonal and right diagonal.
'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        j=len(mat)
        total = 0
        for i in range(j):
            total += mat[i][i] #left diagonal
            total += mat[i][j-i-1] #right diagonal
        if j%2!=0:
            total -= mat[j//2][j//2]

        return total

