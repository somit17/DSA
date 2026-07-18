class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0] and self.find(board,i,j,0,word):
                    return True
        
        return False

    def find(self,board,i,j,idx,word):
        if idx==len(word):
            return True
        if (i < 0 or j < 0 or i >= self.m or j >=self.n or board[i][j]=='$'):
            return False
        if board[i][j]!=word[idx]:
            return False
        temp = board[i][j]
        board[i][j] = '$'
        for values in self.directions:
            i_ = i + values[0]
            j_ = j + values[1]
            if self.find(board,i_,j_,idx+1,word):
                return True
        board[i][j] = temp
        return False