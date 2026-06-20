class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Approach: Work backwards from the last digit, handling carry
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits  # No carry, we're done
            digits[i] = 0  # Set to 0 and continue to handle carry
        
        # If we reach here, all digits were 9 (e.g., [9,9,9] → [1,0,0,0])
        return [1] + digits