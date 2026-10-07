class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j]) == k and j > i:
                    print(f"NUM1 --> {nums[i]}")
                    print(f"NUM2 --> {nums[j]}")
                    count+=1

        return count
        