import re
import json

f = open('inputs/day12.json')
total_sum = 0
with f as puzzle_input:
    line = f.readline()
    x = re.findall(r'-?\d+', line)
    ints = map(int, x)
    total_sum = sum(ints)
    print total_sum

# Duplicate code... could be fixed by creating a generalized iterator
def get_sum(thing):
    total_sum = 0
    if isinstance(thing, dict):
        for k, x in thing.iteritems():
            if k == 'red' or x == 'red': return 0
            if type(x) in [list, dict]: total_sum += get_sum(x)
            elif isinstance(x, int): total_sum += x
    elif isinstance(thing, list):
        for x in thing:
            if type(x) in [list, dict]: total_sum += get_sum(x)
            elif isinstance(x, int): total_sum += x
    return total_sum

print get_sum(json.loads(line))
