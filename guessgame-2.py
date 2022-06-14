num = 34
guess = int(input('输入一个数字：'))
if num == guess:
    print('Good job')
elif num > guess:
    print('too low')
elif num < guess:
    print('too high')
