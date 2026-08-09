class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            ret += matrix.pop(0)

            if matrix and matrix[0]:
                for rows in matrix:
                    ret.append(rows.pop())
                
            if matrix:
                ret += matrix.pop()[::-1]
            
            if matrix and matrix[0]:
                for rows in matrix[::-1]:
                    ret.append(rows.pop(0))
        return ret