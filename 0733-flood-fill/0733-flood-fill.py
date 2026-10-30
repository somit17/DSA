class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc]==color:
            return image
        self.rows = len(image)
        self.cols = len(image[0])
        self.directions = [(0,1),(1,0),(0,-1),(-1,0)]
        self.dfs(image,sr,sc,image[sr][sc],{},color)
        return image
        
    def dfs(self,image,r,c,pixel,visited,color):
        #Bounds
        rowBound = 0 <= r < self.rows
        colBound = 0 <= c < self.cols
        if not rowBound or not colBound:
            return
        
        if image[r][c] != pixel:
            return 

        pos = (r,c)
        if pos in visited:
            return 
        #visited.append(pos)
        image[r][c]=color
        for nr,nc in self.directions:
            newr = r+nr
            newc = c+nc
            self.dfs(image,newr,newc,pixel,visited,color)

        return 

        