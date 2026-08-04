class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        start = 0
        k = len(p)
        p_counter = Counter(p)
        window_counter = Counter(s[:k])
        if window_counter == p_counter:
            result.append(start)
        #print(f'WINDOW - {window_set}')
        for end in range(0,len(s) - k):
            window_counter[s[end]]-=1
            window_counter[s[end + k]]+=1
            if window_counter == p_counter:
                result.append(end+1) 
        return result
        