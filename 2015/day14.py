import re

reindeer = {}
with open('inputs/day14.txt') as puzzle_input:
    for line in puzzle_input.readlines():
        name, speed, flight_time, rest_time = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line).groups()
        reindeer[name] = {
            'speed': int(speed),
            'flight_time': int(flight_time),
            'rest_time': int(rest_time),
            'cycle_time': int(flight_time) + int(rest_time),
            'points': 0
        }

for i in range(1, 2504):
    fastest_reindeer = ''
    farthest_distance = 0
    for name, r in reindeer.iteritems():
        r['distance'] = (i / r['cycle_time']) * (r['speed'] * r['flight_time']) 
        remaining_time = i % r['cycle_time']
        r['distance'] += r['speed'] * (r['flight_time'] if r['flight_time'] <= remaining_time else remaining_time)
        if r['distance'] > farthest_distance:
            farthest_distance = r['distance']
            fastest_reindeer = name
    reindeer[fastest_reindeer]['points'] += 1

print 'Farthest distance: ' + str(max([r['distance'] for i, r in reindeer.iteritems()]))
print 'Highest points: ' + str(max([r['points'] for i, r in reindeer.iteritems()]))
