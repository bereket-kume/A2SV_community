class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix[0])
        myl = []
        j = 0
        while m > 0:
           
            newl = []

            for i in matrix:
                newl.append(i[j])
            m -= 1
            j +=1
            myl.append(newl)
        return myl

