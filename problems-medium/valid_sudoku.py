'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        square=collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in square[(r//3,c//3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True

  '''
  Solution Explained:
  Create 3 dictionaries for rows,columns and squares. For every box in the 9x9 grid, if the number(board[r][c]) is in rows or columns or in a square(We determine the square number by dividing column and row 
  number by 3). If found, return False. Else, add the number to row, column and square based on its respective key value. Column number is the key for cols, row number is the key value for row and square 
  numbers, in the form of (x,y) where x and y are square numbers is its key value. If no repeated values are found, the sudoku is valid and return True.
  '''
