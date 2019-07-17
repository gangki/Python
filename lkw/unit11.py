# 11.8 심사문제: 리스트의 마지막 부분 삭제하기
x = input().split()
del x[-1:-6:-1]
print(x)

#11.9 심사문제: 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결하기
x = input()
y = input()
x_odd = x[1::2]
y_eve = y[0::2]
print(x_odd + y_eve)