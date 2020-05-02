import numpy as np
from numpy.core.multiarray import ndarray


def is_in_safety(board: ndarray, row: int, column: int) -> bool:
    """
    Checks the row, column and diagonals of a candidate queen
    :param board: the board of chess
    :param row: the row of the candidate queen
    :param column: the column of the candidate queen
    :return: a boolean indicating if the cell is free for the queen
    """
    N = len(board)

    # Row and column check
    for i in range(N):
        if board[row][i] or board[i][column]:
            return False

    # Up left diagonal
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j]:
            return False

    # Up right diagonal
    for i, j in zip(range(row, -1, -1), range(column, N, 1)):
        if board[i][j]:
            return False

    # Bottom left diagonal
    for i, j in zip(range(row, N, -1), range(column, -1, -1)):
        if board[i][j]:
            return False

    # Bottom right diagonal
    for i, j in zip(range(row, N, 1), range(column, N, 1)):
        if board[i][j]:
            return False

    return True


def insert_queen(N: int, row: int) -> bool:
    """
    Inserts a queen for each row qnd goes backwards if it is not possible
    :param N: the board dimension
    :param row: the row of the chess board matrix
    :return: a boolean indicating the end of the N queens insertion
    """
    if row == N:
        return True

    for column in range(N):

        if is_in_safety(chess_board, row, column):
            chess_board[row][column] = 1

            if insert_queen(N, row + 1):
                return True

        chess_board[row][column] = 0

    return False


if __name__ == '__main__':
    N = int(input("Enter the desired N dimension of the chess board ... "))
    chess_board = np.zeros(shape=(N, N), dtype=int)
    print(chess_board) if insert_queen(N, 0) else print(f"Placing {N} queens on a {N}x{N} chess board is not possible")
