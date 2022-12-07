with open('day 3 input.txt') as day3Input:
    user_input = day3Input.readlines()
user_input = [text[0:-1] for text in user_input]
# user_input = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
print(user_input)
itemInBothCompartment = ''
itemsInBothCompartment = []

for i in range(len(user_input)):  # 1 now i is 0
    numberOfItemsInEachCompartment = int(len(user_input[i])/2)
    firstCompartment = user_input[i][0: numberOfItemsInEachCompartment]  # vJrwpWtwJgWr
    secondCompartment = user_input[i][numberOfItemsInEachCompartment: 2 * numberOfItemsInEachCompartment + 1]  #hcsFMMfFFhFp
    for j in firstCompartment:  # vJrwpWtwJgWr
        for k in range(len(secondCompartment)):  # 12 k is now 0
            if j == secondCompartment[k]:  # is v = to h?
                itemInBothCompartment = j
                itemsInBothCompartment.append(j)
                break
        if len(itemsInBothCompartment) == i + 1:
            break

print(itemsInBothCompartment)

# calculate priority score
priorityScore = 0
for i in range(len(itemsInBothCompartment)):
    if itemsInBothCompartment[i].isupper() == False:  # lowercase
        indivScore = ord(itemsInBothCompartment[i]) - 96
    else:
        indivScore = ord(itemsInBothCompartment[i]) - 64 + 26
    priorityScore += indivScore
print(priorityScore)

