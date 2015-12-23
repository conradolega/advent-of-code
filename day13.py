import itertools
import re

f = open('inputs/day13.txt')
happiness = {}
with f as puzzle_input:
    for line in f.readlines():
       person, gain, amount, next_person = re.match(r'^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)', line).groups()
       amount = int(amount) * (-1 if gain == 'lose' else 1)
       if (person not in happiness): happiness[person] = {}
       happiness[person][next_person] = amount

def get_greatest_happiness():
    greatest_happiness = 0
    for permutation in itertools.permutations(happiness.keys()):
        total_happiness = 0
        for i, person in enumerate(permutation):
            total_happiness += (happiness[person][permutation[(i + 1) % len(happiness)]]
                + happiness[permutation[(i + 1) % len(happiness)]][person])
        greatest_happiness = max(greatest_happiness, total_happiness)
    return greatest_happiness
print 'Greatest happiness without me: ' + str(get_greatest_happiness())

happiness['me'] = {}
for person in happiness.keys():
    happiness['me'][person] = 0
    happiness[person]['me'] = 0
print 'Greatest happiness with me: ' + str(get_greatest_happiness())
