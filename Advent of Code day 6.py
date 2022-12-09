with open('day 6 input.txt') as day6Input:
    userInput = day6Input.readlines()
# userInput = ['bvwbjplbgvbhsrlpgdmjqwftvncz']

for i in range(0, len(userInput[0]) - 4):
    if userInput[0][i] == userInput[0][i+1] or userInput[0][i] == userInput[0][i+2] or userInput[0][i] == userInput[0][i+3]:
        continue
    elif userInput[0][i+1] == userInput[0][i+2] or userInput[0][i+1] == userInput[0][i+3]:
        continue
    elif userInput[0][i+2] == userInput[0][i+3]:
        continue
    else:
        print(i+4)
        break
