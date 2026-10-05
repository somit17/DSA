class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result = []

        range_list = [False] * (len(nums)+1)

        for num in nums:
            range_list[num]=True

        for i in range(1,len(nums)+1):
            if not range_list[i]:
                result.append(i)

        return result

        