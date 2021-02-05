"""
This module helps to check whether the board is ready to start the game.
"""


def horisontal_check(board: list) -> bool:
    """
    """
    for line in board:
        lst_line = list(line)
        for el in line:
            if el == "*" or el == " ":
                lst_line.remove(el)
        if len(set(lst_line)) != len(lst_line):
            return False
    return True


def invert_board(board: list) -> list:
    """
    """
    inverted_board = ['' for _ in range(len(board))]
    current_sumbol = 0
    while current_sumbol < len(board[0]):
        for line in board:
            inverted_board[current_sumbol] += line[current_sumbol]
        current_sumbol += 1
    return inverted_board


def row_check(board: list) -> bool:
    """
    """
    inverted_board = invert_board(board)
    return horisontal_check(inverted_board)


def color_sells_check(board: list) -> bool:
    """
    """
    colors = ['' for _ in range(5)]
    point = 5
    for line in board[4:9]:
        colors[board.index(line) - 4] += line[point:point + 4]
        point -= 1

    point = 0
    inverted_board = list(reversed(invert_board(board)))
    for line in inverted_board[4:9]:
        colors[inverted_board.index(line) - 4] += line[point:point + 5]
        point += 1

    for color in colors:
        color_sells = [el for el in color if el != ' ']
        if len(set(color_sells)) != len(color_sells):
            return False
    return True


def validate_board(board: list) -> bool:
    """
    """
    if (not horisontal_check(board) or
        not row_check(board) or
            not color_sells_check(board)):
        return False
    return True
