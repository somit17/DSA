class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashmap ={}
        start = 0
        count = 0
        for end in range(len(fruits)):
            print(hashmap)
            hashmap[fruits[end]]=hashmap.get(fruits[end],0) + 1
            while len(hashmap) > 2:
                hashmap[fruits[start]]-=1
                if hashmap[fruits[start]] == 0:
                    del hashmap[fruits[start]]
                start+=1
            count = max(count,end - start + 1)
        return count
        