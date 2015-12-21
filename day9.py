import itertools

f = open('inputs/day9.txt')
paths = {}
least_distance = 999999999
greatest_distance = 0

with f as puzzle_input:
    for line in f.readlines():
        path, distance = line.split(' = ')
        source, destination = path.split(' to ')
        if (source not in paths): paths[source] = {}
        if (destination not in paths): paths[destination] = {}
        paths[source][destination] = int(distance)
        paths[destination][source] = int(distance)

for full_path in itertools.permutations(paths.keys()):
    total_distance = 0
    for i, place in enumerate(full_path):
        if i < len(full_path) - 1:
            total_distance += paths[place][full_path[i + 1]]
    least_distance = min(least_distance, total_distance)
    greatest_distance = max(greatest_distance, total_distance)

print 'Least distance: ' + str(least_distance)
print 'Greatest distance: ' + str(greatest_distance)
