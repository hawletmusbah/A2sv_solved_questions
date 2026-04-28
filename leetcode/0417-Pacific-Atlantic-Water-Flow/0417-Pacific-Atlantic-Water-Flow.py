class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit):
            visit.add((r, c))
            for dr, dc in ((0,1), (0,-1), (1,0), (-1,0)):
                nr, nc = r + dr, c + dc
                # If neighbor is in bounds, not visited, and height is >= current
                if (0 <= nr < R and 0 <= nc < C and 
                    (nr, nc) not in visit and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visit)

        for i in range(R):
            dfs(i, 0, pac)      # Left edge (Pacific)
            dfs(i, C - 1, atl)  # Right edge (Atlantic)
            
        for j in range(C):
            dfs(0, j, pac)      # Top edge (Pacific)
            dfs(R - 1, j, atl)  # Bottom edge (Atlantic)

        # Return coordinates that are in both sets
        return [list(coord) for coord in (pac & atl)]