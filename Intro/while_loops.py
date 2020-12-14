print('Hello human!')

while True:
    user_input = input("> ")
    if user_input == 'quit':
        print('Goodbye human!')
        break
    else:
        print(user_input)

counter = 0
while True:
    print('Hello ' + str(counter))
    counter = counter + 1

    if counter >= 5:
        break