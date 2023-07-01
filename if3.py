print('단위 기호')
inputNum = int(input('input number: '))
result = str(inputNum)

if inputNum >= 1000000000:
    result = str(inputNum // 1000000000) + 'G'
elif inputNum >= 1000000:
    result = str(inputNum // 1000000) + 'M'
elif inputNum >= 1000:
    result = str(inputNum // 1000) + 'K'
elif inputNum >= 0:
    pass

print(result)
