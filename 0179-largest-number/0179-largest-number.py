class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(x,y):
            if x + y > y + x :
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        strs = list(map(str,nums))
        strs.sort(key=cmp_to_key(compare))
        #print(strs)
        if strs[0] == "0":
            return "0"
        
        return "".join(strs)