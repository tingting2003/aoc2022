# A for Rock, B for Paper, and C for Scissors  1 for Rock(X), 2 for Paper(Y), and 3 for Scissors(Z)
singleScore = 0
score = 0

with open('day 2 input.txt') as day2Input:
    user_input = day2Input.readlines()
user_input = [text[0:-1] for text in user_input]
print(user_input)

for i in range(len(user_input)):
    # win
    if user_input[i] in ['A Y','B Z', 'C X']:
        singleScore = 6
    # draw
    elif user_input[i] in ['A X','B Y','C Z']:
        singleScore = 3
    else:
        singleScore = 0
    score += singleScore

for i in range(len(user_input)):
    if user_input[i][2] == 'X':
        singleScore = 1
    elif user_input[i][2] == 'Y':
        singleScore = 2
    elif user_input[i][2] == 'Z':
        singleScore = 3
    score += singleScore

print(score)

# alternative method
# for i in range(len(user_input)):
#     first = ord(user_input[i][0]) - ord('A')
#     second = ord(user_input[i][2]) - ord('X')
#     diff = (first - second) % 3
#     if diff == 2:
#         singleScore = 6
#     elif diff == 1:
#         singleScore = 0
#     else:
#         singleScore = 3
