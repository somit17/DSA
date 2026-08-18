class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        first = nums[0] #1
        full_perms = []
        for perm in self.permute(nums[1:]):
            for i in range(len(perm) + 1):
                full_perms.append(perm[i:] + [first] + perm[:i])

        return full_perms



# [
#     [2,3],
#     [3,2]
# ]

# [
#     [1,2,3]
#     [2,1,3]
#     [2,3,1]
#     [1,3,2]
#     [3,1,2]
#     [3,2,1]
# ]

        self.permute(nums[1:])
        