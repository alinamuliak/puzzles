# puzzles
Second task in first lab.

The playing field of the logic puzzle has a square shape of 9 × 9 cells. The playing field contains cells of different colors that are used in the game and white areas that are not used for the game.

This module helps to set whether the logic puzzle playing field is ready to start the game. The cells of the playing field must be filled in according to the following rules before the start of the game:

1. The colored cells of each line must contain numbers from 1 to 9 without repetition.

2. The colored cells of each column must contain the numbers 1 to 9 without repetition.

3. Each block of cells of the same color must contain numbers from 1 to 9 without repetition.

The validate_board (board) function - the main function - returns a Boolean value.