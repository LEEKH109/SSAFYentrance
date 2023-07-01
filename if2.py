print('나이에 따른 세대 구분 (1)')
inputAge = int(input('What year were you born?: '))
gen = None

if inputAge <= 1924:
    gen = 'the Greatest Generation'
elif inputAge <= 1945:
    gen = 'the Silent Generation'
elif inputAge <= 1964:
    gen = 'a baby boomer'
elif inputAge <= 1980:
    gen = 'a Gen X'
elif inputAge <= 1996:
    gen = 'a millennial'
else:
    gen = 'a Gen Z'

print(f"You're {gen}.")  # f포멧팅, f-string으로 검색
