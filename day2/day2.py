#! python

f = open('input.txt', 'r')

twice = 0
threetime = 0
for line in f:
    multiples = {}
    for letter in line.strip():
        if letter in multiples.keys():
            multiples[letter] += 1
        else:
            multiples[letter] = 1
    once2 = False
    once3 = False
    for m in multiples:
        if multiples[m] == 2 and not once2:
            once2 = True
            twice += 1
        elif multiples[m] == 3 and not once3:
            once3 = True
            threetime += 1

res = twice * threetime
print('RES: %s' % res)
    
