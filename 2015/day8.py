f = open('inputs/day8.txt')
difference1 = 0
difference2 = 0
with f as puzzle_input:
    for line in puzzle_input.readlines():
        difference1 += len(line) - 1 - len(eval(line))
        difference2 += len(line) - 1 + line.count('"') + line.count('\\') + 2 - (len(line) - 1)

print 'Answer to part 1: ' + str(difference1)
print 'Answer to part 2: ' + str(difference2)
