class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.explore(1,n,k,[])
        return self.result

    def explore(self,start,n,k,comb):
        if k == 0:
            self.result.append(comb[:])
            return 
        if start > n:
            return
        #Take element
        comb.append(start)
        self.explore(start+1,n,k-1,comb)
        #Skip element
        comb.pop()
        self.explore(start+1,n,k,comb)