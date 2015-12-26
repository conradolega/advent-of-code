import re

ingredients = []
totals = [0, 0, 0, 0]
all_calories = []
with open('inputs/day15.txt') as puzzle_input:
    for line in puzzle_input.readlines():
        name, capacity, durability, flavor, texture, calories = re.match(r'(\w+): capacity (-?\d), durability (-?\d), flavor (-?\d), texture (-?\d), calories (-?\d)', line).groups()
        ingredients.append([
            int(capacity),
            int(durability),
            int(flavor),
            int(texture),
        ])
        all_calories.append(int(calories))

highest_score = 0
highest_score_with_calories = 0
for i in range(0, 100):
    for j in range(0, 101 - i):
        for k in range(0, 101 - i - j):
            l = (100 - i - j - k)
            totals[0] = [i * d for d in ingredients[0]]
            totals[1] = [j * d for d in ingredients[1]]
            totals[2] = [k * d for d in ingredients[2]]
            totals[3] = [l * d for d in ingredients[3]]
            total_score = [sum(d[a] for d in totals) for a in range(0, 4)]
            total_score = reduce(lambda x, y: x * y if (y > 0) else 0, total_score, 1)
            highest_score = max(highest_score, total_score)
            if (all_calories[0] * i +
                all_calories[1] * j +
                all_calories[2] * k +
                all_calories[3] * l == 500):
                highest_score_with_calories = max(highest_score_with_calories, total_score)

print 'Highest score: ' + str(highest_score)
print 'Highest score for 500 calories: ' + str(highest_score_with_calories)
