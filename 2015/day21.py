import itertools

boss = {
    'hit_points': 100.0,
    'damage': 8,
    'armor': 2
}

player = {
    'hit_points': 100.0,
    'damage': 0,
    'armor': 0,
    'gold_spent': 0
}

weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]
armor = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
    (0, 0, 0)
]
rings = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
    (0, 0, 0)
]

def simulate(player, boss):
    player_net_damage = max(player['damage'] - boss['armor'], 1)
    boss_net_damage = max(boss['damage'] - player['armor'], 1)
    return boss['hit_points'] / player_net_damage <= player['hit_points'] / boss_net_damage

least_winning_cost = 999
greatest_losing_cost = 0
least_combo = tuple()
worst_combo = tuple()
for i in itertools.product(weapons, armor, rings, rings):
    if i[2] == i[3]: continue
    player['hit_points'] = 100.0
    boss['hit_points'] = 100.0
    player['damage'] = sum([i[j][1] for j in [0, 2, 3]])
    player['armor'] = sum([i[j][2] for j in [1, 2, 3]])
    player['gold_spent'] = sum([j[0] for j in i])
    if simulate(player, boss):
        least_winning_cost = min(least_winning_cost, player['gold_spent'])
        if player['gold_spent'] == least_winning_cost: least_combo = i
    else:
        greatest_losing_cost = max(greatest_losing_cost, player['gold_spent'])
        if player['gold_spent'] == greatest_losing_cost: worst_combo = i

print 'Least cost to win: ' + str(least_winning_cost)
print 'Greatest cost to lose: ' + str(greatest_losing_cost)
