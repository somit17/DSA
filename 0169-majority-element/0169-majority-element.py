class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums)
        for k,v in counter.items():
            print(f'K->{k}->{n}')
            print(f'V->{v}')
            if v > n // 2:
                return k
        return -1