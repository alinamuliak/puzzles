"""
This module helps to check whether the board is ready to start the game.
"""


def horisontal_check(board: list) -> bool:
    """
    Check if any line in board has repeatable number.
    If yes, return False, otherwise - True.

    >>> horisontal_check(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 2****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    True
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
    Return the inverted board.
    (Rows become lines, and lines become rows.)

    >>> invert_board(["**34**",\
"354*4*",\
"97*769",\
"123456",\
"7*6*5*",\
"8889*4"])
    ['*39178', '*572*8', '34*368', '4*74*9', '*4655*', '**96*4']
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
    Check if any row in the board has repeatedly numbers.
    If yes, return False, otherwise - True.

    >>> row_check(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    False
    """
    inverted_board = invert_board(board)
    return horisontal_check(inverted_board)


def color_sells_check(board: list) -> bool:
    """
    Check if there is repeatedly numbers in one-colour-sells.
    If yes, return False, otherwise - True.

    >>> color_sells_check(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    True
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
    Check whether the board is ready to start the game.
    The cells of the playing field must be filled according to the following rules
    before the start of the game:
    1) The colored cells of each line must contain numbers from 1 to 9 without repetition.
    2) The colored cells of each column must contain the numbers 1 to 9 without repetition.
    3) Each block of cells of the same color must contain numbers from 1 to 9 without repetition.

    >>> validate_board(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    False
    >>> validate_board(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 2****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    True
    """
    if (not horisontal_check(board) or
        not row_check(board) or
        not color_sells_check(board)):
        return False
    return True
