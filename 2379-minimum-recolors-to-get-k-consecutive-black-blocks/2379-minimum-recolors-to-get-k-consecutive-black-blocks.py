class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start = 0
        white_count = 0
        min_ops = float('inf')
    
        for end in range(len(blocks)):
            # Expand window: add the new block
            if blocks[end] == 'W':
                white_count += 1
            
            # Shrink window if its size exceeds k
            while end - start + 1 > k:
                if blocks[start] == 'W':
                    white_count -= 1
                start += 1
            
            # When window size is exactly k, we have a valid window
            if end - start + 1 == k:
                min_ops = min(min_ops, white_count)
    
        return min_ops