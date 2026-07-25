class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_counter = Counter(magazine)
        ran_counter = Counter(ransomNote)
        for k,v in ran_counter.items():
            if ran_counter[k]> mag_counter.get(k,0):
                return False
            
        return True
        