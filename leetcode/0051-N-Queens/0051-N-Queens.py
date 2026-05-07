class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def isSafe(row, col, board):
            c_col ,c_row = col,row
            while c_row >= 0 and c_col >= 0 :
                if board[c_row][c_col] == 'Q':
                    return False
                c_row -= 1
                c_col -= 1


            c_col ,c_row = col,row
            while c_col >= 0 :
                if board[c_row][c_col] == 'Q':
                    return False
                c_col -= 1

            c_col ,c_row = col,row
            while c_col >= 0 and c_row < n :
                if board[c_row][c_col] == 'Q':
                    return False
                c_row += 1
                c_col -= 1
            return True

        def solve(col, board, ans, n):
            #base case 
            if col == n:
                ans.append(["".join(row) for row in board ])
                return 

            for row in range(n):
                if isSafe(row,col,board):
                    board[row][col] = 'Q'
                    solve(col + 1,board,ans,n)

                    board[row][col] = '.'

        ans = []
        # Initialize an n x n board with '.'
        board = [['.' for _ in range(n)] for _ in range(n)]
        solve(0, board, ans, n)
        return ans

# Example usage:
# sol = Solution()
# print(sol.solveNQueens(4))