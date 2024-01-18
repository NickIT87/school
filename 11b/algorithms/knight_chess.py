from typing import List

def is_valid_move(board: List[List[int]], x: int, y: int, visited: List[List[bool]]) -> bool:
    """Перевірка, чи хід коня відповідає правилам та чи клітина не була вже відвідана."""
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and not visited[x][y]

def knight_tour_util(board: List[List[int]], row: int, col: int, move_count: int,
                      x_moves: List[int], y_moves: List[int], visited: List[List[bool]]) -> bool:
    """Рекурсивна функція для знаходження шляху коня по шаховій дошці."""
    if move_count == len(board) * len(board[0]):
        # Успішно завершено обхід
        return True

    for i in range(8):
        next_row = row + x_moves[i]
        next_col = col + y_moves[i]

        if is_valid_move(board, next_row, next_col, visited):
            visited[next_row][next_col] = True
            board[next_row][next_col] = move_count + 1

            if knight_tour_util(board, next_row, next_col, move_count + 1,
                                x_moves, y_moves, visited):
                return True

            visited[next_row][next_col] = False
            board[next_row][next_col] = 0

    return False

def knight_tour(board_size: int, start_row: int, start_col: int) -> None:
    """Знаходження шляху коня по шаховій дошці та виведення результату."""
    board: List[List[int]] = [[0 for _ in range(board_size)] for _ in range(board_size)]
    visited: List[List[bool]] = [[False for _ in range(board_size)] for _ in range(board_size)]

    board[start_row][start_col] = 1
    visited[start_row][start_col] = True

    x_moves: List[int] = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves: List[int] = [1, 2, 2, 1, -1, -2, -2, -1]

    if knight_tour_util(board, start_row, start_col, 1, x_moves, y_moves, visited):
        print("Шлях коня:")
        for row in board:
            print(row)
    else:
        print("Розв'язок не знайдено.")

# Приклад виклику функції для дошки розміром 5x5 з початковим положенням (2, 2)
knight_tour(5, 2, 2)
