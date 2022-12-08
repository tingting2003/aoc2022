with open('day 4 input.txt') as day4Input:
    user_input = day4Input.readlines()
user_input = [i[0:-1] for i in user_input]
# user_input = ['98-99, 3-97', '23-72,23-72']
print(user_input)

final_user_input = []
# split the pairs
for i in range(len(user_input)):
    user_input1 = user_input[i].split(',')
    final_user_input.append(user_input1)
print(final_user_input)

indiv_section = []
for i in range(len(final_user_input)):
    final_user_input1 = final_user_input[i][0].split('-')
    indiv_section.append(final_user_input1)
    final_user_input1 = final_user_input[i][1].split('-')
    indiv_section.append(final_user_input1)
print(indiv_section)
print(indiv_section[0])

answer = 0
for i in range(0, len(indiv_section), 2):  # 1 len = ['98', '99']
    if int(indiv_section[i][0]) in range(int(indiv_section[i+1][0]), int(indiv_section[i+1][1]) + 1) and int(indiv_section[i][1]) in range(int(indiv_section[i+1][0]), int(indiv_section[i+1][1]) + 1):
        answer += 1
    elif int(indiv_section[i+1][0]) in range(int(indiv_section[i][0]), int(indiv_section[i][1]) + 1) and int(indiv_section[i+1][1]) in range(int(indiv_section[i][0]), int(indiv_section[i][1]) + 1):
        answer += 1

print(answer)