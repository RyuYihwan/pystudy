# print
print("""Hello""")
print('''Hello!''')

# Separator 옵션
print('T', 'E', 'S', 'T', sep='')
print('2020', '02', '22', sep='-')
print('dd', 'google.com', sep='@')

# end 옵션
print('Welcome To', end=' ')
print('the black parade', end='')
print(' piano notes')
print('============')

# format 사용 [], {}, ()
print('{} and {}'.format('a', 'b'))
print('{0} and {1} and {0}'.format('a', 'b'))
print('{a} are {b}'.format(a='You', b='Me'))

# %s: 문자, %d: 정수, %f: 실수
print("%s's favorite number is %d" % ('Eunki', 7))
print("Test1: %5d, Price: %4.2f" % (776, 6534.123213))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123213))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123213))

# escape 문자 '\'
