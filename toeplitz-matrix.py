class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        val = False
        for i in range(len(matrix)-1):
            for j in range(len(matrix[i])-1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    val = True
                    break

        return val==False

