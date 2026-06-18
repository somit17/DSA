class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        for i in range(0,cols):
            temp = []
            for j in range(0,rows):
                temp.append(matrix[j][i])
            result.append(temp)
        print(result)
        return result