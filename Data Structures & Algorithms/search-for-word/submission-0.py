class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        sol=[]
        visited=set()
        def backtrack(row,col,i):
            if i==len(word):
                return True
            
            if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or board[row][col]!=word[i] or (row,col) in visited:
                return False
            
            visited.add((row,col))

            found=backtrack(row+1,col,i+1) or backtrack(row-1,col,i+1) or backtrack(row,col+1,i+1) or backtrack(row,col-1,i+1)

            visited.remove((row,col))

            return found
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True
        return False

        