for i in range(1, 101): # 1. 1에서 100까지 출력
    if i % 15 == 0:
        print('FizzBuzz', end = ' ') # 3과 5의 공배수는 FizzBuzz출력
    elif i % 3 == 0:
        print('Fizz', end = ' ') # 2. 3의 배수는 Fizz 출력
    elif i % 5 == 0:
        print('Buzz', end = ' ') # 3. 5의 배수는 Buzz 출력
    else:
        print(i, end = ' ')

# 코드 단축하기

for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)