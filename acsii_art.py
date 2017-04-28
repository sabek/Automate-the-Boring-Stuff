grid = [['.', '.', '.', '.', '.','.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.','.']]

lines = [['' for x in range(9)] for y in range(7)]

for x in range(len(grid)):
    for y in range(len(grid[x])):
        lines[y][x] = grid[x][y]

for x in range(len(lines)):
    for y in range(len(lines[x])):
        print(lines[x][y], end='')
    print("")
