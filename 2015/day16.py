import re

sues = {}
actual = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}
actual_set = set(actual.items())
actual_without_ranges = {
    'children': 3,
    'samoyeds': 2,
    'akitas': 0,
    'vizslas': 0,
    'cars': 2,
    'perfumes': 1
}
actual_without_ranges_set = set(actual_without_ranges.items())
greater_than = {
    'cats': 7,
    'trees': 3,
} 
less_than = {
    'pomeranians': 3,
    'goldfish': 5
}
with open('inputs/day16.txt') as puzzle_input:
    for line in puzzle_input.readlines():
        number, property_1, property_1_number, property_2, property_2_number, property_3, property_3_number = re.match(r'^Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line).groups()
        sues[number] = {
            property_1: int(property_1_number),
            property_2: int(property_2_number),
            property_3: int(property_3_number)
        }
        sue_set = set(sues[number].items())
        if len(actual_set.intersection(sue_set)) == 3: first_guess = number
        difference = sue_set - actual_without_ranges_set
        original_difference = set(difference)
        for k, v in original_difference:
            if k in actual_without_ranges: continue
            if ((k in greater_than and greater_than[k] < v) or
                (k in less_than and less_than[k] > v)):
                difference.remove((k, v))
        if len(difference) == 0: second_guess = number

print 'First guess: ' + str(first_guess)
print 'Second guess: ' + str(second_guess)
