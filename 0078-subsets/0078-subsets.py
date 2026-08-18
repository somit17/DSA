class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [ [] ] #[[]]

        first_element = nums[0] # 1
        subs_without_first = self.subsets(nums[1:]) # [[]]
        subs_with_first = []

        for sub in subs_without_first:
            subs_with_first.append([first_element,*sub])  

        return subs_without_first + subs_with_first


#[1]
        