class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = Counter(nums1)
        result = []
        for num in nums2:
            if num in hash_map and hash_map[num] > 0:
                hash_map[num] = hash_map[num] - 1
                result.append(num)
        return result