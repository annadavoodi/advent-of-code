from aocd import data

'''
Part 1:

A = rock, B = paper, C = scissors
X = rock, Y = paper, Z = scissors

Winning: highest total score
total score = sum of round scores
round score = different points for choice + different points for outcome
Points for choice: rock = 1, paper = 2, scissors = 3
Points for outcome: lose = 0, draw = 3, win = 6 

Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.

Total score?
'''

round_list = [row.split(' ') for row in data.split('\n')]
total_score = 0

for round in round_list:
    opponent = round[0]
    you = round[1]

    round_score = 0
                                    
    if opponent == 'A': #op rock
        if you == 'X': #you rock -> draw
            round_score = 1+3
            total_score += round_score
        elif you == 'Y': #you paper -> win
            round_score = 2+6
            total_score += round_score
        else: #you scis -> lose
            round_score = 3
            total_score += round_score

    elif opponent == 'B': #op paper
        if you == 'X': #you rock -> lose
            round_score = 1
            total_score += round_score
        elif you == 'Y': #you paper -> draw
            round_score = 2+3
            total_score += round_score
        else: #you scis -> win
            round_score = 3+6
            total_score += round_score

    else: #op scissors
        if you == 'X': #you rock -> win
            round_score = 1+6
            total_score += round_score
        elif you == 'Y': #you paper -> lose
            round_score = 2
            total_score += round_score
        else: #you scis -> draw
            round_score = 3+3
            total_score += round_score
    
print('Your total score is: \t{}'.format(total_score))

'''
Part 2: 

A = rock, B = paper, C = scissors
X = lose, Y = draw, Z = win

Winning: highest total score
total score = sum of round scores
round score = different points for choice + different points for outcome
Points for choice: rock = 1, paper = 2, scissors = 3
Points for outcome: lose = 0, draw = 3, win = 6 

Total score?
'''

total_score = 0

for round in round_list:

    opponent = round[0]
    you = round[1]

    round_score = 0

    if you == 'Z': #if we are supposed to win
        if opponent == 'A': #if opponent = rock -> you paper
            round_score = 2+6
            total_score += round_score
        elif opponent == 'B':#if opponent = paper -> you scissor
            round_score = 3+6
            total_score += round_score
        else: #if opponent = scissor -> you rock
            round_score = 1+6
            total_score += round_score

    if you == 'Y': #if we are supposed to draw
        if opponent == 'A': #if opponent = rock -> you rock
            round_score = 1+3
            total_score += round_score
        elif opponent == 'B':#if opponent = paper -> you paper
            round_score = 2+3
            total_score += round_score
        else: #if opponent = scissor -> you scissor
            round_score = 3+3
            total_score += round_score

    if you == 'X': #if we are supposed to lose
        if opponent == 'A': #if opponent = rock -> you scissor
            round_score = 3
            total_score += round_score
        elif opponent == 'B': #if opponent = paper -> you rock
            round_score = 1
            total_score += round_score
        else: #if opponent = scissor -> you paper
            round_score = 2
            total_score += round_score

print('Your total score is: \t{}'.format(total_score))
