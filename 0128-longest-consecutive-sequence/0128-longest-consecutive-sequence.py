class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hash_map = {} #Boolean represents whether its start or not so by default we kept is True
        for num in nums:
            hash_map[num] = True

        for num in nums:
            if num - 1 in hash_map:
                hash_map[num] = False
        max_len = float('-inf')
        for num in hash_map:
            if hash_map[num]:
                length = 1
                while (num + length) in hash_map:
                    length+=1
                max_len = max(max_len,length)
        return max_len