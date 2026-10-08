class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return self.divide_conquer(nums)
    
    def divide_conquer(self,nums):
        if len(nums)<=1:
            return nums

        mid = len(nums) // 2

        left_portion = nums[:mid]
        right_portion = nums[mid:]

        #Recursively
        left_half = self.divide_conquer(left_portion)
        right_half = self.divide_conquer(right_portion)
        return self.merge(left_half,right_half)

    def merge(self,left,right):

        result = []
        i=j=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

        