class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            mask = bit << (31 - i)
            result |= mask
        return result