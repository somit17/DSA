class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        

        #hash_map and Sorting
        hash_map = {}
        for h,n in zip(heights,names):
            hash_map[h] = n

        sorted_res = sorted(hash_map.keys(),reverse = True)
        result = []
        for h in sorted_res:
            result.append(hash_map[h])

        return result