from hashlib import md5

puzzle_input = 'ckczppom'
md5_hash = ''
number = 0

while md5(puzzle_input + str(number)).hexdigest()[0:5] != '00000':
    number += 1

print 'First number to generate hash starting with 00000: ' + str(number)

number = 0
md5_hash = ''
while md5(puzzle_input + str(number)).hexdigest()[0:6] != '000000':
    number += 1
print 'First number to generate hash starting with 000000: ' + str(number)
