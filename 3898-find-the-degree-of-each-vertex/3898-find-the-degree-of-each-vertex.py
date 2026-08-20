class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:

        adj_list = {}
        n = len(matrix)

        for idx,row in enumerate(matrix):
            adj_list[idx]=[]
            for idx2,element in enumerate(row):
                if element == 1:
                    adj_list[idx].append(idx2)
        result = [0] * n
        for node in adj_list:
            result[node]=len(adj_list[node])
        print(result) 
        return result