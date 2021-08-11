# SudokuSolver  
## Introduction:  
In this assignment we are asked to write a program that will solve a given sudoku puzzle, in the
first task we assume the puzzle is legal, and in the second task we make sure it is, as well as
check for multiple possible solutions.  
## The algorithm:  
There are a couple of ways to solve a sudoku using programming, first there is the naive way,
which has a long runtime, and there is the backtracking algorithm, which still takes long on large
instances, but has better runtime than the naive approach.  
I implemented the backtracking algorithm to solve sudoku, using mainly 3 functions:  
Find_empty: a function that finds an empty cell on the board.  
Valid: a function that checks if a certain value is valid in a certain cell on the board.  
Solve: the main recursive function that utilises find_empty and valid to solve the entire board.  
## How to run:  
On windows, from the command line in the directory you placed the assignment in, run the
command “python task<X>.py input\<instance>.sudoku where X is the number of the task you
are trying to run, and <instance> is the name of the instance you’d like to run.
I have provided some instances in input folder, and their respectful results in output folder.
