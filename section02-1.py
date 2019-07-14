# section02-1
# 파이썬 기초 코팅
# print 구문의 이해

# 기본 출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019', '07', '14', sep='-')
print('niceman', 'google.com', sep='@')

print()

# end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

print()

# format 사용
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{a} and {b}'.format(a='You', b='Me'))
print("%s's favorite number is %d" % ('Eunki', 7))
# %s: 문자, %d: 정수, %f: 실수

print()
