class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
     

        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # Base case: out of bounds or not an 'O'
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            
            # Mark the cell as visited/safe
            board[r][c] = "#"
            
            # Traverse neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Run DFS from all 'O's on the border
        for r in range(rows):
            dfs(r, 0)            # Left edge
            dfs(r, cols - 1)     # Right edge

        for c in range(cols):
            dfs(0, c)            # Top edge
            dfs(rows - 1, c)     # Bottom edge

        # Step 2: Traverse the board and flip cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    # This 'O' was not connected to the border
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    # This was a safe 'O', restore it
                    board[r][c] = 'O'