from aocd import data 

#Helper function

def priority_sum(sim_list):
    '''
    Calculate priority sum given a list of priority elements
    '''
    prio_sum = 0
    for letter in sim_list:
        if letter[0].isupper():
            prio_sum += ord(letter[0])-38
        elif letter[0].islower():
            prio_sum += ord(letter[0])-96

    return prio_sum

'''
Part 1:

Find sum of prio of similarities of the compartments in each rucksack.
'''

rucksack = data.split('\n')

split_rucksacks = []
for sack in rucksack:
    compartment1 = slice(0,len(sack)//2)
    compartment2 = slice(len(sack)//2,len(sack))
    split_rucksacks.append([sack[slice(0,len(sack)//2)], sack[slice(len(sack)//2,len(sack))]])

sims = [[key for key in set(rucksack[0]) & set(rucksack[1])] for rucksack in split_rucksacks]

sum = priority_sum(sims)

print('The priority sum of items found in both compartments for each rucksack is :\n\t {}'.format(sum))

'''
Part 2: 

Find total sum of prio of similarities for each group.
Each group consists of three sequential rucksacks.

'''
i = 0
groups = []
while i <= len(rucksack)-3:
    group = [rucksack[i], rucksack[i+1], rucksack[i+2]]
    groups.append(group)
    i += 3

badge = [[key for key in set(rucksack[0]) & set(rucksack[1]) & set(rucksack[2])] for rucksack in groups]

sum = priority_sum(badge)

print('The priority sum of badges for each group is:\n\t {}'.format(sum))