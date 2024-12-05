import fileinput

lines = [line.rstrip() for line in fileinput.input()]

rules_raw, updates_raw = [], []

for i in range(len(lines)):
    if lines[i] == "":
        rules_raw = lines[:i]
        updates_raw = lines[i+1:]


rules = {}
for rule in rules_raw:
    x, y = [int(i) for i in rule.split('|')]
    if x not in rules:
        rules[x] = [y]
    else:
        rules[x].append(y)

updates = []
for update in updates_raw:
    updates.append([int(x) for x in update.split(',')])


invalid = []
for update in updates:
    correct = True
    for i in range(1, len(update)):
        for j in range(0, i):
            if update[j] in rules.get(update[i], []):
                correct = False
                invalid.append(update)
                break
        if not correct:
            break

for update in invalid:
    correct = False
    while not correct:
        correct = True
        for i in range(1, len(update)):
            for j in range(0, i):
                if update[j] in rules.get(update[i], []):
                    correct = False
                    update[i], update[j] = update[j], update[i]
                    



result = 0
for update in invalid:
    result += update[len(update)//2]

print(result)
