with open('day 5 input.txt') as day5Input:
    user_input = day5Input.readlines()

position = 0
for i in user_input:
    if not i[0] == 'm':
        position += 1
    if i[0] == 'm':
        break
print(position)
crates = user_input[0: position - 2]
instructions = user_input[position:]

# idk how to handle the input :((
