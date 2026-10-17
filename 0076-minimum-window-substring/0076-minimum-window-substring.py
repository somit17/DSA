class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counts = Counter(t)
        window_counts = Counter()
        required = len(target_counts)
        formed = 0
        l = 0
        min_len = float('inf')
        ans = ''
        for r in range(len(s)):
            window_counts[s[r]]+=1

            if s[r] in target_counts and window_counts[s[r]] == target_counts[s[r]]:
                formed+=1

            while formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = s[l:r+1] # Save the actual substring here!
                window_counts[s[l]]-=1
                if s[l] in target_counts and window_counts[s[l]] < target_counts[s[l]]:
                    formed-=1
                l+=1
            #ans=s[l:r+1]
        return ans
                