def is_safe(board,row,col):
    for i in range(row):
        if board[i] ==col or abs(board[i]-col) == abs(i-row):
            return False
    return True

def solve_n_queens(n):
    board = [-1]*n
   
    def backtrack(row):
         if row == n:
             print(board)
             return
         for col in range(n):
             if is_safe (board,row,col):
                board[row] = col
                backtrack(row+1)
    backtrack(0)
solve_n_queens(8)
