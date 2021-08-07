N = int(input())

array = []

# append는 배열 끝에 삽입
# insert는 몇번째 칸에 삽입할지 지정가능 (숫자, 값)
for i in range(0, N):
    num = int(input())
    array.append(num)

# 버블정렬
for i in range(len(array)-1, 0, -1):
    for j in range(0, i):
        if(array[j] > array[j+1]):
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp

for i in range(0, len(array)):
    print(array[i])