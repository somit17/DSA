class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # The Notebook: stores { character: last_seen_index }
        last_seen = {}
        start = 0
        longest = 0

        for end in range(len(s)):
            char = s[end]

            # 1. CHECK THE NOTEBOOK
            # If we've seen this character before, we might need to jump
            if char in last_seen:
                # The "Security Guard" rule: 
                # Only jump if the duplicate is INSIDE our current window.
                # This prevents us from jumping backwards (the Trap Case).
                start = max(start, last_seen[char] + 1)

            # 2. UPDATE LONGEST
            # Window size is always (right - left + 1)
            longest = max(longest, end - start + 1)

            # 3. RECORD POSITION
            # Update the notebook with the current index of this character
            last_seen[char] = end

        return longest