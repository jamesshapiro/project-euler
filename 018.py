#!/usr/bin/env python3 -tt

grid = [[75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

values = {}

for i in range(len(grid)):
    for j in range(len(grid[i])):
        cellValue = grid[i][j]
        if i == 0:
            values[(i,j)] = cellValue
        elif j == 0:
            values[(i,j)] = cellValue + values[(i-1,j)]
        elif j == len(grid[i]) - 1:
            values[(i,j)] = cellValue + values[(i-1,j-1)]
        else:
            values[(i,j)] = cellValue + max(values[(i-1,j)], values[(i-1,j-1)])

print(max(values[(len(grid)-1,x)] for x in range(len(grid[len(grid)-1]) - 1)))
