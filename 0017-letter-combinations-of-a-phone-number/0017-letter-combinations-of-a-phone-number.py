class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:  # Handle empty input
            return []
        n = len(digits)
        hash_map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        result = []
        def backtrack(idx,comb):
            if len(comb)==len(digits):
                result.append("".join(comb))
                return 
            digit = digits[idx]
            chars = hash_map[digit]
            for char in chars:
                comb.append(char)
                backtrack(idx+1,comb)
                comb.pop() 
        backtrack(0,[])
        return result