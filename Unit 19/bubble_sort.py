# 오름차순 버블 소트
aList = [5, 4, 21, 3, 15, 2, 93, 11, 20]
aList = list(map(int,input('숫자를 입력하세요: ').split()))
print(aList)

for i in range(0, len(aList)-1):
    for k in range(i+1, len(aList)):
        if aList[i] > aList[k]:
            aList[i], aList[k] = aList[k], aList[i]
print(aList)

# 내림차순 버블 소트 (<만 변경)
aList = [5, 4, 21, 3, 15, 2, 93, 11, 20]
aList = list(map(int,input('숫자를 입력하세요: ').split()))
print(aList)

for i in range(0, len(aList)-1):
    for k in range(i+1, len(aList)):
        if aList[i] < aList[k]:
            aList[i], aList[k] = aList[k], aList[i]
print(aList)