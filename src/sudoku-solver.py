import numpy as np

# Sudoku Solver
# Accepts a 9 matrix of numbers, with "0" as a placeholder for blank spaces
# Then, checks which numbers 1-9 the first zero can legally be replaced with
# Then, calls itself, with the first zero replaced with valid numbers 1-9


def sudoku_solver(grid, x, y):

    # double loop to find zero
    for i in range(x, 9):
        for j in range(0, 9):
            if grid[i, j] == 0:         # found a zero

                # get list of numbers in row, column, square
                row = grid[i]
                col = grid[:, j]

                m = (i // 3) * 3
                n = (j // 3) * 3
                sqr = grid[m:m+3, n:n+3]

                # flatten 2D array into 1D array
                sqr = sqr.flatten()

                # check that numbers (1-9) are not already in row, column, or square
                # recursively check remaining grid for any currently valid option
                for k in range(1, 10):
                    if not (any(row == k) or any(col == k) or any(sqr[:] == k)):
                        grid[i, j] = k          # change zero value in grid to k
                        if sudoku_solver(grid, i, j):
                            return True
                grid[i, j] = 0
                return False

    for r in range(9):
        print(grid[r])
    return True


print("Enter numbers from Sudoku puzzle, replacing blanks with zeros: ")

a = []

for i in range(9):          # A for loop for user data entry
    line = input()
    chars = map(int, [char for char in line])
    a.append(list(chars))

    grid = np.array(a)

sudoku_solver(grid, 0, 0)
