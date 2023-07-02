import os
os.system('clear')

print('입력받은 숫자만큼 반복하기(for)')
input = int(input('입력: '))

for i in range(1, input+1): # range 함수는 시작 숫자는 포함 끝나는 숫자는 포함하지 않게 작동해서 (1,10)으로 범위를 지정하면 1~9까지만 범위를 구성한다.
    print(input)