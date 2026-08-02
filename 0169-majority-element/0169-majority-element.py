class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_num = Counter(nums)
        n = len(nums)
        for k,v in hash_num.items():
            if v > n // 2:
                return k
        return -1