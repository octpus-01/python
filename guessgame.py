num = 34
run = True

while run:
    guess = int(input('Please guess a number:'))
    if guess == num:
        print('well done you guess it')
        run = False
    elif guess > num:
        print('The number lower than this one')
    else:
        print('The number is higher than this one')
print('finish')
