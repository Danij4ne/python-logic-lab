
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
