from copy import deepcopy

boss = {
    'hit_points': 71,
    'damage': 10
}

player = {
    'hit_points': 50,
    'mana': 500,
    'mana_cost': 0,
    'armor': 0,
    'effects': [False, False, False, False, False],
    'cooldowns': [0, 0, 0, 0, 0],
    'used': [],
    'turn': 0
}

spells = [
    (53, 4, 0, 0, 0, 1, 'Magic Missile'),
    (73, 2, 2, 0, 0, 1, 'Drain'),
    (113, 0, 0, 7, 0, 6, 'Shield'),
    (173, 3, 0, 0, 0, 6, 'Poison'),
    (229, 0, 0, 0, 101, 5, 'Recharge'),
]

states = set()
least_cost = 99999
def simulate(player, boss, hard_mode):
    global least_cost
    if player['mana'] < 53: return

    # Effect phase
    if hard_mode == True:
        player['hit_points'] -= 1
        if player['hit_points'] == 0: return

    for index, effect in enumerate(player['effects']):
        if effect == False: continue
        boss['hit_points'] -= spells[index][1]
        player['armor'] = player['armor'] or spells[index][3]
        player['mana'] += spells[index][4]
        player['cooldowns'][index] -= 1
        if player['cooldowns'][index] == 0:
            if index == 2: player['armor'] = 0
            player['effects'][index] = False

    original_player = deepcopy(player)
    original_boss = deepcopy(boss)
    if boss['hit_points'] <= 0:
        least_cost = min(player['mana_cost'], least_cost)
        return

    for i, spell in enumerate(spells):
        player = deepcopy(original_player)
        boss = deepcopy(original_boss)
        if player['mana'] < spell[0] or player['effects'][i]: continue
        if player['mana_cost'] + spell[0] >= least_cost: continue
               
        # Attack phase
        player['mana'] -= spell[0]
        player['mana_cost'] += spell[0]
        player['used'].append(spell[6])
        if spell[5] == 1:
            boss['hit_points'] -= spell[1]
            player['hit_points'] += spell[2]
        else:
            player['effects'][i] = True
            player['cooldowns'][i] = spell[5]
            
        if boss['hit_points'] <= 0:
            least_cost = min(player['mana_cost'], least_cost)
            continue

        for index, effect in enumerate(player['effects']):
            if effect == False: continue
            boss['hit_points'] -= spells[index][1]
            player['armor'] = player['armor'] or spells[index][3]
            player['mana'] += spells[index][4]
            player['cooldowns'][index] -= 1
            if player['cooldowns'][index] == 0:
                if index == 2: player['armor'] = 0
                player['effects'][index] = False

        if boss['hit_points'] <= 0:
            least_cost = min(player['mana_cost'], least_cost)
            continue

        # Defense phase
        player['hit_points'] -= max(boss['damage'] - player['armor'], 1)
        if player['hit_points'] <= 0: continue
        
        simulate(player, boss, hard_mode)

simulate(player, boss, False)
print 'Part 1: ' + str(least_cost)
least_cost = 99999
simulate(player, boss, True)
print 'Part 2: ' + str(least_cost)

