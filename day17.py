bins = []
with open('inputs/day17.txt') as puzzle_input:
    for line in puzzle_input.readlines():
        bins.append(int(line))

length = len(bins)
format_string = '0' + str(length) + 'b'
part1_answer = 0
minimum_number = len(bins)
part2_answer = 0
for i in range(0, pow(2, len(bins))):
    combination_string = list(format(i, format_string))
    combination = [b for x, b in enumerate(bins) if combination_string[x] == '1']
    if sum(combination) == 150:
        part1_answer += 1
        if len(combination) < minimum_number:
            minimum_number = len(combination)
            part2_answer = 0
        if len(combination) == minimum_number: part2_answer += 1

print 'Number of combinations: ' + str(part1_answer)
print 'Number of combinations with the minimum number: ' + str(part2_answer)
