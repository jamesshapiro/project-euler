#!/usr/bin/env python3 -tt

grid_length = 1001
grid = [list() for x in range(grid_length)]
for i in range(grid_length):
    grid[i] = [0 for x in range(grid_length)]

center = grid_length // 2
i = 2
grid[center][center] = 1
for j in range((grid_length + 1) // 2):
    row = center - j + 1
    col = center + j
    for k in range(j*2 - 1):
        grid[row][col] = i
        i += 1
        row += 1
    for k in range(j*2):
        grid[row][col] = i
        i += 1
        col -= 1
    for k in range(j*2):
        grid[row][col] = i
        i += 1
        row -= 1
    for k in range(j*2):
        grid[row][col] = i
        i += 1
        col += 1
    if i != 2:
        grid[row][col] = i
        i += 1

first_diagonal = sum(grid[x][x] for x in range(grid_length))
second_diagonal = sum(grid[x][grid_length-x-1] for x in range(grid_length))
print(first_diagonal + second_diagonal - grid[center][center])
