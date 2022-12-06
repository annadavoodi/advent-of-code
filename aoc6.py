from aocd import data

'''
Part 1:
'''

for i in range(len(data)-4):
    s = data[i:i+4]
    instance = []
    unique = 0
    for char in s:
        if char not in instance:
            instance.append(char)
        else:
            unique += 1
    if unique == 0:
        disc = i+4
        break

print('{} charachters processed'.format(disc))

'''
Part 2:
'''

for i in range(len(data)-14):
    s = data[i:i+14]
    instance = []
    unique = 0
    for char in s:
        if char not in instance:
            instance.append(char)
        else:
            unique += 1
    if unique == 0:
        disc = i+14
        break

print('{} charachters processed'.format(disc))