class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        n = len(matrix)
        m = len(matrix[0])
        listt = []
        for irow , row in enumerate(matrix):
            for iele, element in enumerate(row):
                if element == 0:
                   listt.append([irow,iele])
        

        for i in listt:
            matrix[i[0]] = [0] * m
            for row in matrix:
                row[i[1]] = 0