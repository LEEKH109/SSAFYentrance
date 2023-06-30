print('얌체공\n')
input = int(input('input:'))

num = 1
result = input
while num <= 10:
    result *= 0.6
    print(num, round(result, 4))
    num += 1
