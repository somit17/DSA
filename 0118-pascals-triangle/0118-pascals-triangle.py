class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for i in range(numRows):
            current = [1]
            for j in range(1,i):
                current.append(result[i-1][j]+result[i-1][j-1])
            if i > 0:
                current.append(1)
            result.append(current)
        return result