with open('inputs/day6.txt') as input_file:
    inputs = input_file.read().splitlines()

most_common = ''
least_common = ''
for i in range(0, len(inputs[0])):
    column = [message[i] for message in inputs]
    counts = {c: column.count(c) for c in set(column)}
    rank = sorted(counts, key=counts.get, reverse=True)
    most_common += rank[0]
    least_common += rank[-1]

print(most_common)
print(least_common)
