with open('inputs/day1.txt') as input_file:
    steps = input_file.readline()[:-1].split(', ')

x = 0
y = 0
sequence = [0, -1, 0, 1]
direction = (0, 3)
for index, step in enumerate(steps):
    if step[0] == 'L':
        direction = ((direction[0] - 1) % 4, (direction[1] - 1) % 4)
    else:
        direction = ((direction[0] + 1) % 4, (direction[1] + 1) % 4)

    if sequence[direction[0]] != 0:
        x += int(step[1:]) * sequence[direction[0]]
    else:
        y += int(step[1:]) * sequence[direction[1]]

print(abs(x) + abs(y))
