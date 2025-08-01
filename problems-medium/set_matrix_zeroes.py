'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
'''

# Non-Optimised Solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indices = []
        for i,row in enumerate(matrix):
            for j,val in enumerate(row):
                if val==0:
                    indices.append((i,j))

        for x, y in indices:
            for j in range(len(matrix[0])):
                matrix[x][j] = 0
            for i in range(len(matrix)):
                matrix[i][y] = 0
