import re

replacements = []
results = set()
string = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'
with open('inputs/day19.txt') as puzzle_input:
    for line in puzzle_input.readlines():
        replacements.append(tuple(line[:-1].split(' => ')))

for replacement in replacements:
    start = 0
    search = True
    while search:
        search = re.search(replacement[0], string[start:])
        if search:
            results.add(string[:start] + re.sub(replacement[0], replacement[1], string[start:], count = 1))
            start += search.end()
print 'Number of results: ' + str(len(results))

steps = 0
while string != 'e':
    for replacement in replacements:
        new_string = re.sub(replacement[1], replacement[0], string, count = 1)
        if string != new_string:
            steps += 1
            string = new_string

print 'Number of steps: ' + str(steps)
