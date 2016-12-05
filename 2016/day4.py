import re

with open('inputs/day4.txt') as input_file:
    inputs = [re.match(r'([a-z-]+)(\d+)\[(\w+)\]', line).groups() for line in input_file.read().splitlines()]

sector_id_sum = 0
north_pole_sector_id = 0
for room in inputs:
    name = room[0]
    checksum = room[2]
    counts = [(-name.count(c), c) for c in set(name) - set('-')]
    most_common = sorted(counts)
    most_common = list(map(lambda x: x[1], most_common))
    expected_code = ''.join(most_common[0:5])
    if expected_code == checksum:
        sector_id = int(room[1])
        sector_id_sum += sector_id
        shifted = ''.join(list(map(lambda c: chr(97 + (ord(c) % 97 +sector_id) % 26) if c != '-' else ' ', name)))
        if shifted == 'northpole object storage ':
            north_pole_sector_id = sector_id

print(sector_id_sum)
print(north_pole_sector_id)
