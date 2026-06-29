class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(arr):
            if len(arr)<=1:
                return arr

            #Divide 
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:] 

            #Conquer
            left_half = merge_sort(left)
            right_half = merge_sort(right)
            return merge(left_half,right_half)

        def merge(left,right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            #Add remaining if present
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        return merge_sort(nums)
        