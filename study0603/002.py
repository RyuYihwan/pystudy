# import this
import sys

# 파이썬 기본 인코딩(UTF-8)
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is Goodboy!')

# 변수 선언(한글도 가능하긴 하지만 미권장)
myName = 'Goodboy'

# 조건문
if myName == 'Goodboy':
    print('OK')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i * j)

# 함수 선언(한글도 가능하긴 하지만 미권장)
def greeting():
    print("안녕하세요")

greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))