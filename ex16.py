# 주어진 문자열의 공백을 ‘,’(콤마) 로 변경 후 출력하세요.
# ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'p', 'e', 'n', 'c', 'i', 'l']

list = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'p', 'e', 'n', 'c', 'i', 'l']

result = ''

for word in list:
    result +=word

print(result)



list[4] = ","
list[7] = ","
list[9] = ","

result2 =''

for word in list:
    result2 +=word

print(result2)
