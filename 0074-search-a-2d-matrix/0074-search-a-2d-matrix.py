class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix)-1
        print(f'R===={right}')
        search_row = []
        while left <= right:
            mid = (left + right) // 2
            if target <= matrix[mid][-1]:
                search_row = matrix[mid]
                right = mid - 1
            else:
                #search_row = matrix[mid+1]
                left = mid+1
        
        if left == len(matrix):
            return False

        search_row = matrix[left]      
        print(search_row)
        l,r = 0,len(search_row)-1
        while l<=r:
            mid = (l+r)//2
            if target == search_row[mid]:
                return True
            elif search_row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False