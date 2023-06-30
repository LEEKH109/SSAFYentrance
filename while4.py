number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10
    rev = rev * 10 + rem
    number = number // 10

print(rev)
# START) num = 853
# 1) rem = 8 rev = 8 num = 35
# 2) rem = 5 rev = 85 num = 3
# 3) rem = 3 rev = 853 num = 0 => STOP
