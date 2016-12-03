with open('inputs/day1.txt') as input_file:
    steps = input_file.readline()[:-1].split(', ')

x = 0
y = 0
sequence = [0, -1, 0, 1]
direction = (0, 3)
visited = []
first_visited = []

def check_if_visited(x, y):
    if first_visited == [] and (x, y) in visited:
        first_visited.append((x, y))
    else:
        visited.append((x, y))


for index, step in enumerate(steps):
    if step[0] == 'L':
        direction = ((direction[0] - 1) % 4, (direction[1] - 1) % 4)
    else:
        direction = ((direction[0] + 1) % 4, (direction[1] + 1) % 4)

    length = int(step[1:])
    if sequence[direction[0]] != 0:
        for i in range(0, length):
            check_if_visited(x + sequence[direction[0]] * i, y)
        x += int(length) * sequence[direction[0]]
    else:
        for i in range(0, length):
            check_if_visited(x, y + sequence[direction[1]] * i)
        y += int(length) * sequence[direction[1]]


print(abs(x) + abs(y))
print(abs(first_visited[0][0]) + abs(first_visited[0][1]))
