class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        idx = 0
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[idx]:
                    if self.dfs(board,row,col,idx,word):
                        return True
        return False

    def dfs(self,board,r,c,idx,word):

        if idx == len(word):
            return True

        #Row  and Col Bounds
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == '$':
            return False
        
        if board[r][c]!=word[idx]:
            return False

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        temp = board[r][c]
        board[r][c] = '$'
        for direction in directions:
            nr,nc = direction
            if self.dfs(board,nr+r,nc+c,idx+1,word):
                return True
        board[r][c] = temp
        return False   

        