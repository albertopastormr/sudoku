# sudoku
## About

Terminal python classic sudoku game app.

## Sudoku rules

Sudoku is a number placing puzzle game based on a 9x9 matrix with several given numbers (random numbers generated at the beginning). The object is to place the numbers 1 to 9 in the empty squares (three 3x3 matrix contained in the main 9x9 matrix) so that each row, each column and each square contains the same number only once.

## Usage

Every play command is composed of three integers: __x__, __y__ and __p__.

-> `x` the number of the row where you want to place your number. Remember to type a number that is between 1 and 9.

-> `y` the number of the column where you want to place your number. Remember to type a number that is between 1 and 9.

-> `p` the number you want to place at the intersection of `x`-`y`. Remember to type a number that is between 1 and 9.


The application will inform you if your play can't be executed.
This occurs, mainly, because of two reasons: it doesn't follow the rules specified above or the numbers you typed are not in the valid range (1-9).

Type x: _-1_ to stop the execution of the current game.
