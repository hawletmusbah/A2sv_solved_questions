class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # total number of diagonal = m+n-1
        row = len(mat)
        col = len(mat[0])
        res = [[]  for _ in range(row +col -1)]
        # print(res)
        for r in range(row):
            for c in range(col):
                res[r+c].append(mat[r][c])
        # print(res)
        ans = []
        for i in range(len(res)):
            if i % 2 == 0:
                ans.extend(res[i][::-1])
            else:
                ans.extend(res[i])

        # print(ans)
        return ans