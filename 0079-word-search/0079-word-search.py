class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    if self.dfs(board,r,c,word,0):
                        return True

        return False
                
        
    def dfs(self,board,r,c,word,idx):
        if idx == len(word):
            return True
        
        #Bounds Check
        rowsBound = 0 <= r < len(board)
        colsBound = 0 <= c < len(board[0])

        if not rowsBound or not colsBound:
            return False

        if board[r][c]!=word[idx]:
            return False

        
        #Temp store
        temp = board[r][c]
        board[r][c] = '#'

        found = (self.dfs(board,r+1,c,word,idx+1) or
                self.dfs(board,r-1,c,word,idx+1) or
                self.dfs(board,r,c+1,word,idx+1) or
                self.dfs(board,r,c-1,word,idx+1))

        board[r][c] = temp
        return found