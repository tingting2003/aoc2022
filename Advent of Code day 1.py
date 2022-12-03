calories_each = 0
calories_max = 0

with open('input.txt') as hello:
    while True:
        user_input = hello.readline()
        if user_input == '':
            break
        if user_input != '\n':
            calories_each += int(user_input)
        else:
            if calories_each > calories_max:
                calories_max = calories_each
            calories_each = 0

print(calories_max)