from itertools import groupby

puzzle_input = '1321131112'
for i in range(0, 50):
    puzzle_input = ''.join([str(len(list(g))) + k for k, g in groupby(puzzle_input)])
    if i == 39: print '40: ' + str(len(puzzle_input))
    if i == 49: print '50: ' + str(len(puzzle_input))
