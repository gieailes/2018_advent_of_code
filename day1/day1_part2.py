#! python

f = open('input.txt', 'r')

lines = []
for line in f:
    lines.append(line[:-1])

#print(lines)
res = 0
logged_frequencies = [0]
found_it = False
print('\n RES: %s' % res)

while found_it == False:
    for action in lines:
        if action:
            if action[0] == '+':
                print('res:%s plus %s' % (res, action[1:]))
                res = res + int(action[1:])
                if res in logged_frequencies:
                    print('FOUND IT! Duplicate frequency - %s' % res)
                    found_it = True
                    break
                else:
                    logged_frequencies.append(res)
            elif action[0] == '-':
                print('res:%s minus %s' % (res, action[1:]))
                res = res - int(action[1:])
                if res in logged_frequencies:
                    print('FOUND IT! Duplicate frequency - %s' % res)
                    found_it = True
                    break
                else:
                    logged_frequencies.append(res)
            else:
                print('WTF: %s' % action)

print('\n RES: %s' % res)

