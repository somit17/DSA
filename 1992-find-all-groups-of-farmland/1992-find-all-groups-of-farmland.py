class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        rows = len(land)
        cols = len(land[0])
        result = []
        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1:
                    top_edge = (r == 0) or (land[r-1][c] == 0)
                    left_edge = (c == 0) or (land[r][c-1]==0)
                    if top_edge and left_edge:
                        right = c
                        while right + 1 < cols and land[r][right + 1] == 1:
                            right+=1
                        bottom = r
                        while bottom + 1 < rows and land[bottom + 1][c] == 1:
                            bottom+=1
                        
                        result.append([r, c, bottom, right])
        return result
        