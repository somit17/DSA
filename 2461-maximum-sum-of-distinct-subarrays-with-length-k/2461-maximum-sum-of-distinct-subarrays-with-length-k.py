from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        start = 0
        window = Counter()
        max_sum = 0
        current_sum = 0
        
        for end in range(len(nums)):
            window[nums[end]] += 1
            current_sum += nums[end]

            # The "Bad Window" Logic
            while window[nums[end]] > 1 or (end - start + 1) > k:
                current_sum -= nums[start]
                window[nums[start]] -= 1
                if window[nums[start]] == 0:
                    del window[nums[start]]
                start += 1

            # The "Exact-Size" Verification
            if (end - start + 1) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum