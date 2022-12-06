from aocd import data

inp = '    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2'

crates = [element for element in data.split('\n') if not element.startswith('m') and not element == '']
numbers = [int(number) for number in crates[-1] if not number == ' ']
rows = [crates[i].split(' ') for i in range(len(crates)-1)]

crates_d = {}
temp_row = []
temp_rows = []

c = 0
for row in rows:
    while c < len(row):
        if row[c] == '':
            temp_row.append(row[c])
            c += 4
        else:
            temp_row.append(row[c])
            c += 1
    temp_rows.append(temp_row)
    temp_row = []
    c = 0

for number in numbers:
    for row_i in range(len(temp_rows)):
        elem = temp_rows[row_i][number-1]
        if elem != '':
            if number in crates_d:
                crates_d[number].append(elem)
            else:
                crates_d[number] = [elem]

for key,value in crates_d.items():
    value.reverse()
    crates_d[key] = value


instructions = [element for element in data.split('\n') if element.startswith('m')]
instructions = [string.split() for string in instructions]
amount = [int(instruction[1]) for instruction in instructions]
start = [int(instruction[3]) for instruction in instructions]
stop = [int(instruction[5]) for instruction in instructions]
''' PART 1:
for i in range(len(amount)):
    #move x from y to z
    x = amount[i]
    y = start[i]
    z = stop[i]
    while x > 0:
        last = crates_d[y][-1]
        del crates_d[y][-1]
        crates_d[z].append(last)
        x -= 1
'''

for i in range(len(amount)):
    #move x from y to z
    temp_list = []
    x = amount[i]
    y = start[i]
    z = stop[i]
    moving_list = crates_d[y][-x:]
    del crates_d[y][-x:]
    for crate in moving_list:
        crates_d[z].append(crate)
        
str_list = ''.join(crates_d[key][-1][1] for key in crates_d)
print('The crates on top are: \t{}'.format(str_list))

