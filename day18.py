import copy

grid = [[False for i in range(0, 102)] for j in range(0, 102)]
with open('inputs/day18.txt') as puzzle_input:
    for i, line in enumerate(puzzle_input.readlines()):
        for j, char in enumerate(list(line[:-1])):
            grid[i + 1][j + 1] = char == '#'
original_grid = copy.deepcopy(grid)

for iteration in range(0, 100):
    temp_grid = copy.deepcopy(grid)
    for i in range(1, 101):
        for j in range(1, 101):
            live_neighbors = [
                temp_grid[i - 1][j - 1],
                temp_grid[i - 1][j],
                temp_grid[i - 1][j + 1],
                temp_grid[i][j + 1],
                temp_grid[i + 1][j + 1],
                temp_grid[i + 1][j],
                temp_grid[i + 1][j - 1],
                temp_grid[i][j - 1]].count(True)
            if live_neighbors != 2 and live_neighbors != 3 and temp_grid[i][j]:
                grid[i][j] = False
            elif live_neighbors == 3 and temp_grid[i][j] == False:
                grid[i][j] = True

print 'Answer to part 1: ' + str(sum([row.count(True) for row in grid]))

grid = copy.deepcopy(original_grid)
for iteration in range(0, 100):
    grid[1][1] = grid[1][100] = grid[100][1] = grid[100][100] = True
    temp_grid = copy.deepcopy(grid)
    for i in range(1, 101):
        for j in range(1, 101):
            live_neighbors = [
                temp_grid[i - 1][j - 1],
                temp_grid[i - 1][j],
                temp_grid[i - 1][j + 1],
                temp_grid[i][j + 1],
                temp_grid[i + 1][j + 1],
                temp_grid[i + 1][j],
                temp_grid[i + 1][j - 1],
                temp_grid[i][j - 1]].count(True)
            if live_neighbors != 2 and live_neighbors != 3 and temp_grid[i][j]:
                grid[i][j] = False
            elif live_neighbors == 3 and temp_grid[i][j] == False:
                grid[i][j] = True
    grid[1][1] = grid[1][100] = grid[100][1] = grid[100][100] = True

print 'Answer to part 2: ' + str(sum([row.count(True) for row in grid]))
