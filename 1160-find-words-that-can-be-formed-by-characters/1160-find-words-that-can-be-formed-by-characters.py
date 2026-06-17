class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashmap = [0] * 26
        for ch in chars:
            hashmap[ord(ch)-ord('a')]+=1
        print(hashmap)
        result = 0
        for word in words:
            word_count = [0] * 26
            for ch in word:
                word_count[ord(ch)-ord('a')]+=1
            can_form = True
            for i in range(0,26):
                if word_count[i] > hashmap[i]:
                    can_form = False
                    break
            if can_form:
                result+=len(word)   
        return result