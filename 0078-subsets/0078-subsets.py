class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(index,path):
            if index == len(nums):
                result.append(path[:])  
                return     
            path.append(nums[index]) #Take
            dfs(index+1,path)    #Explore by taking element
            path.pop()           #Popped
            dfs(index+1,path)    #Explore by popping element

        result = []
        dfs(0,[])
        return result
    
        