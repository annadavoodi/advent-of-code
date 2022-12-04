from aocd import data

'''
Part 1:

Check how many assignment pairs have full overlaps.

Part 2:

Check how many assignments have some overlaps

'''

pairs = [assignment.split(',') for assignment in data.split('\n')]

overlap1 = 0; overlap2 = 0
for pair in pairs:
    range_first = [int(pair[0].split('-')[0]), int(pair[0].split('-')[1])]
    if range_first[0] != range_first[1]:
        first_list = list(range(range_first[0], range_first[1] + 1))
    else:
        first_list = [range_first[0]]
    
    range_second = [int(pair[1].split('-')[0]), int(pair[1].split('-')[1])]
    if range_second[0] != range_second[1]:
        second_list = list(range(range_second[0], range_second[1] + 1))
    else:
        second_list = [range_second[0]]

    first_contains_second = all(item in first_list for item in second_list) 
    second_contains_first = all(item in second_list for item in first_list) 
    if first_contains_second or second_contains_first:
        overlap1 += 1

    any_overlaps = any(item in first_list for item in second_list) 
    if any_overlaps:
        overlap2 += 1
    

print(f'The amount of full overlaps in group assignments are: \t {overlap1}')
print(f'The amount of overlaps in group assignments are: \t {overlap2}')