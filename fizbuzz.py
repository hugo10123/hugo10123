import time
x = 1
while True:
    if x % 15 == 0:
        print('FizzBuzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fizz')
    else:
        print(x)
    x += 1