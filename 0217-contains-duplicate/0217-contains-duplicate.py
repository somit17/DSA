class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash_map = Counter(nums)
        # for k,v in hash_map.items():
        #     if v > 1:
        #         return True
        #     print(f'KEY - {k}')
        #     print(f'V - {v}')
        # return False

        #Approach 2 
        my_set = set(nums)
        return len(my_set)!=len(nums)