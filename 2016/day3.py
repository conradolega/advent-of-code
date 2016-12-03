with open('inputs/day3.txt') as input_file:
    inputs = [line.strip().split() for line in input_file.read().splitlines()]

number = 0
for triangle in inputs:
    x = int(triangle[0])
    y = int(triangle[1])
    z = int(triangle[2])

    if x + y > z and x + z > y and y + z > x:
        number += 1

print(number)

number = 0
for j in range(0, 3):
    for i in range(0, len(inputs) / 3):
        x = int(inputs[i * 3][j])
        y = int(inputs[i * 3 + 1][j])
        z = int(inputs[i * 3 + 2][j])

        if x + y > z and x + z > y and y + z > x:
            number += 1

print(number)
