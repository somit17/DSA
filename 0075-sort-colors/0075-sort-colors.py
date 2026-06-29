class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #using merge sort
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            #recursively
            left = merge_sort(left)
            right = merge_sort(right)
            return merge(left,right)
        
        def merge(left,right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    result.append(right[j])
                    j+=1
                else:
                    result.append(left[i])
                    i+=1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        sorted_arr = merge_sort(nums)
        nums[:] = sorted_arr
