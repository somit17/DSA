class Solution:
    def findLucky(self, arr: list[int]) -> int:
        counter = Counter(arr)
        max_num = float('-inf')

        for k,v in counter.items():
            if k == v:
               max_num = max(max_num,k)

        return -1 if max_num == float('-inf') else max_num


        