import os
os.system('clear')

print('제곱표(for)')

input = int(input('input: '))

for i in range(1, input+1):
    print(i, i*i)