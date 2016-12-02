puzzle_input = 29000000
sum_of_factors = puzzle_input / 10

part1_answer = 0
part2_answer = 0
factors = []
i = 0
while part1_answer == 0 or part2_answer == 0:
    i += 1
    small_factors = [x for x in xrange(1, int(i ** 0.5) + 1) if i % x == 0]
    big_factors = [i / x for x in small_factors if x * x != i]
    factors = small_factors + big_factors
    if part1_answer == 0 and sum(factors) >= sum_of_factors: part1_answer = i
    factors = [x for x in factors if i / x <= 50]
    if part2_answer == 0 and sum(factors) * 11 >= puzzle_input: part2_answer = i

print 'Answer to part 1: ' + str(part1_answer)
print 'Answer to part 2: ' + str(part2_answer)
