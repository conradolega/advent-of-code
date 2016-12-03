with open('inputs/day2.txt') as input_file:
    steps = input_file.read().splitlines()

code = ''
start = 5
for step in steps:
    for direction in step:
        if direction == 'U' and start > 3:
            start -= 3
        elif direction == 'D' and start < 7:
            start += 3
        elif direction == 'L' and start % 3 != 1:
            start -= 1
        elif direction == 'R' and start % 3 != 0:
            start += 1
    code += str(start)

print(code)

keypad = 'XX1XXX234X56789XABCXXXDXX'
code = ''
start = 10 # position of 5

for step in steps:
    for direction in step:
        if direction == 'U':
            movement = -5
        elif direction == 'D':
            movement = 5
        elif direction == 'L':
            movement = -1
        elif direction == 'R':
            movement = 1

        if start + movement >= 2 and start + movement <= 22 and keypad[start + movement] != 'X':
            start += movement
    code += str(keypad[start])

print(code)
