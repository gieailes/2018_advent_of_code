#! python

f = open('input.txt', 'r')

lines = []
for line in f:
    lines.append(line[:-1])

#print(lines)
res = 0
print('\n RES: %s' % res)

for action in lines:
    if action:
        if action[0] == '+':
            print('res:%s plus %s' % (res, action[1:]))
            res = res + int(action[1:])
        elif action[0] == '-':
            print('res:%s minus %s' % (res, action[1:]))
            res = res - int(action[1:])
        else:
            print('WTF: %s' % action)

print('\n RES: %s' % res)

