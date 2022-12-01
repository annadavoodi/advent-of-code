from aocd import data

'''
PART 1: 
    Find the maximal amount of calories carried by an elf.
'''
list_elf_cal = [s.split() for s in data.split('\n\n') if s]
list_elf_cal2 = [[int(i) for i in sublist] for sublist in list_elf_cal]

calsum_per_elf = []

cals = 0
for elf in list_elf_cal2:
    for i in range(len(elf)):
        cals += elf[i]
    calsum_per_elf.append(cals)
    cals = 0

calsum_per_elf.sort()

print('The maximal amount of calories carried by an elf is: \t{}'.format(calsum_per_elf[-1]))

'''
PART 2: 
    Find the top three Elves carrying the most Calories. 
    How many Calories are those Elves carrying in total?
'''
calsum_top_three = sum(calsum_per_elf[-3:])
print('\nThe sum of the top three carrying elves is: \t{}'.format(calsum_top_three))