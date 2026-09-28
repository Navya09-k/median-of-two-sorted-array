class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def f():
            best = None; opts = None
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        b = [board[i][j] for i in range(r//3*3,r//3*3+3) for j in range(c//3*3,c//3*3+3)]
                        x = [n for n in '123456789' if n not in board[r] and all(board[i][c]!=n for i in range(9)) and n not in b]
                        if not x: return False
                        if opts is None or len(x) < len(opts): best,opts=(r,c),x
            if best is None: return True
            r,c=best
            for n in opts:
                board[r][c]=n
                if f(): return True
                board[r][c]='.'
            return False
        f()