class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digit = (digits[i] + carry)  % 10
            carry = (digits[i] + carry) // 10
            print(f'Digit -->{digit}')
            print(f'C -- > {carry}')
            result.insert(0,digit)
        if carry == 1:
            result.insert(0,carry)
        return result