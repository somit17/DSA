class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a3 = []
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                a3.append(nums2[j])
                j+=1
            else:
                a3.append(nums1[i])
                i+=1
        
        while i < len(nums1):
            a3.append(nums1[i])
            i+=1
        while j < len(nums2):
            a3.append(nums2[j])
            j+=1
        total = len(nums1) + len(nums2)
        #print(a3[total//2])
        isEven = (total & 1) == 0
        if isEven:
            return (a3[total//2 - 1] + a3[total // 2] )  / 2
        return a3[total // 2]