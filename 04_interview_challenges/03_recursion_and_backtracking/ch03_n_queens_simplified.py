
"""
CH03 - N-Queens (Simplified)

Description:
    The N-Queens problem asks how to place N queens on an N×N chessboard
    so that none of them can attack each other. In chess, a queen can move
    horizontally, vertically, and diagonally.

    For this simplified version:
        - Solve the problem for N = 4.
        - Find ONE valid arrangement.
        - Print the board with 'Q' for queens and '.' for empty spaces.

Requirements:
    - Use recursion and backtracking.
    - Represent the board in any structure (list of lists, etc.).
    - Place queens row by row.
    - Only place a queen if it's safe:
        - No other queen in the same column.
        - No other queen in diagonal positions.
    - If a placement fails later, backtrack and try another position.

Notes:
    - Only one valid solution is required.
    - No need to handle larger N unless desired.

Example (one valid output for N=4):
    . Q . .
    . . . Q
    Q . . .
    . . Q .
"""

# TODO:
# 1. Represent the board (e.g., 4x4).
# 2. Write a function to check if a position is safe.
# 3. Use recursion to place queens row by row.
# 4. Backtrack when a placement fails.
# 5. Print one valid solution.



def print_board(board):
    for row in board:
        print(" ".join(row))

def is_safe(board, row, col, n):
    # Check column (rows above only, since we place row by row)
    for r in range(row):
        if board[r][col] == "Q":
            return False

    # Check upper-left diagonal
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == "Q":
            return False
        r -= 1
        c -= 1

    # Check upper-right diagonal
    r, c = row - 1, col + 1
    while r >= 0 and c < n:
        if board[r][c] == "Q":
            return False
        r -= 1
        c += 1

    return True

def solve_n_queens(board, row, n):
    # Base case: placed queens in all rows
    if row == n:
        return True

    # Try each column in this row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"

            # Recurse to place next row
            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = "."

    return False

def main():
    n = 4
    board = [["." for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print_board(board)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()