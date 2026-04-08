class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        coloumn = len(img[0])
        res = [[0] * coloumn for _ in range(row)]
        for r in range(row):
            for c in range(coloumn):
                total = 0
                count = 0
                for i in range(r-1 ,r + 2):
                    for j in range(c-1 , c+2):
                        if i < 0 or i == row or j < 0 or j == coloumn:
                            continue
                        total += img[i][j]
                        count += 1
                res[r][c] = total//count
        return res