import matplotlib.pyplot as plt


def is_safe(board, row, col, n):
    # Check if a queen can be placed in the current position
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # Found a solution, add it to the list
        solutions.append(board[:])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row] = 0  # Backtrack


def plot_chessboard(solution):
    n = len(solution)
    chessboard = [[0 for _ in range(n)] for _ in range(n)]

    for row, col in enumerate(solution):
        chessboard[row][col] = 1

    plt.imshow(chessboard, cmap='Blues', interpolation='none')
    plt.xticks([])
    plt.yticks([])

    for i in range(n):
        for j in range(n):
            if chessboard[i][j] == 1:
                plt.text(j, i, 'Q', color='red', ha='center', va='center', fontsize=12)

    plt.show()


def solve_n_queens(n):
    solutions = []
    board = [0] * n
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


# Example usage:
n = 8
solutions = solve_n_queens(n)

print(solutions[0])
#print(len(solutions))

plot_chessboard(solutions[0])

# for solution in solutions:
#     plot_chessboard(solution)
