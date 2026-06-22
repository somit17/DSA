class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        n = len(nums) // 2
        for key,value in hashmap.items():
            if value > n:
                return key
        return 0