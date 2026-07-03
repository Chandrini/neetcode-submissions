class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited=set()
        cols=set()
        diags=set()
        anti=set()
        res=[]
        board = [["."] * n for _ in range(n)]        

        def back(row):
            if row==n:
                res.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or (row+col) in anti or (row-col) in diags:
                    continue
                board[row][col]="Q"
                
                cols.add(col)
                anti.add(row+col)
                diags.add((row-col))

                back(row+1)
                board[row][col]="."
                cols.remove(col)
                diags.remove(row-col)
                anti.remove(row+col)
        back(0)
        return res


