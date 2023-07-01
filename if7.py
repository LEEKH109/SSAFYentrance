import os
os.system('clear')

print('나이에 따른 세대 구분 (2)')
# inputAge = int(input('What year were you born?: '))
# gen = None

# if inputAge <= 1924:
#     gen = 'the Greatest Generation'
# elif inputAge <= 1945:
#     gen = 'the Silent Generation'
# elif inputAge <= 1954:
#     born = input('Are you Korean?(y/n): ')
#     if born == 'y':
#         gen = 'the Silent Generation'
#     elif born == 'n':
#         gen = 'a baby boomer'
# elif inputAge == 1964:
#     born = input('Are you Korean?(y/n): ')
#     if born == 'y':
#         gen = 'a Gen X'
#     elif born == 'n':
#         gen = 'a baby boomer'
# elif inputAge < 1964:
#     gen = 'a baby boomer'
# elif inputAge <= 1980:
#     gen = 'a Gen X'
# elif inputAge <= 1996:
#     gen = 'a millennial'
# else:
#     gen = 'a Gen Z'

# print(f"You're {gen}.")  # f포멧팅, f-string으로 검색

# 레퍼런스 코드
y = int(input('What year were you born? '))

gen = None
if y <= 1924:
    gen = 'the Greatest Generation'
elif y <= 1945 or (
    y <= 1954 and input("Are you Korean?(y/n) ").lower()[0] == 'y'
):
    gen = 'the Silent Generation'
elif y <= 1963 or (
    y <= 1964 and input("Are you Korean?(y/n) ").lower()[0] != 'y'
):
    gen = 'a baby boomer'
elif y <= 1980:
    gen = 'a Gen X'
elif y <= 1996:
    gen = 'a millennial'
else:
    gen = 'a Gen Z'

print(f"You're {gen}.")
