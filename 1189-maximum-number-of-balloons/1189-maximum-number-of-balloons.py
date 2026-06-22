class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = 'balloon'
        ballon_map = Counter(s)
        hashmap = {}
        for ch in text:
            if ch in s:
                hashmap[ch] = hashmap.get(ch,0)+1
        print(f"B- {ballon_map}") 
        print(hashmap) 
        count = float('inf')
        for char,needed in ballon_map.items():
            available = hashmap.get(char,0)
            count  = min(count,available // needed)
        
        return count

        