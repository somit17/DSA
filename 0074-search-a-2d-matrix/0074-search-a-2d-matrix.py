class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rl,rr = 0 , len(matrix) - 1
        row_mid = 0
        while rl <= rr:
            mid = (rl + rr) // 2
            #print(f'MID - {matrix[mid]} and resyl = {matrix[mid][0] >= target and matrix[mid][-1] > target}')
            if  matrix[mid][-1] >= target:
                print(f'MID R- {matrix[mid]}')
                #return mid
                row_mid = mid
                rr = mid - 1
            else:
                rl = mid + 1
        
        cl,cr = 0,len(matrix[0]) -1 
        while cl <= cr:
            mid = (cl + cr) // 2
            print(f'MID - {matrix[row_mid][mid]}')
            if matrix[row_mid][mid] == target:
                return True
            elif matrix[row_mid][mid] > target:
                cr = mid - 1
            else:
                cl = mid + 1
        return False
        
        