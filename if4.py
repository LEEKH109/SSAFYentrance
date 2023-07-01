print('양수만 덧셈하기')

sum = 0
while True:
    num = int(input('please input number: '))
    if num < 0:
        break
    else:
        sum += num
print(f'sum: {sum}')
