# 파이썬 예외처리의 이해

# SyntaxError: 잘못된 문법

# NameError: 참조변수 없음

# ZeroDivisionError: 0 나누기 에러
# print(10 / 0)

# IndexError: 인덱스 범위 오버
l = [10, 20, 30]
print(l[0])
# print(l[3])

# KeyError
dic = {'name': 'Kim'}
# print(dic['hobby'])
print(dic.get('hobby'))  # None

# AttributeError: 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time

print(time.time())
# print(time.month())

# ValueError: 참조 값이 없을 때 발생
x = [1, 4, 6]
# x.remove(10)
# x.index(10)

# FileNotFoundError
# f = open('test.txt', 'r')  # 예외 발생

# TypeError

x = [1, 2]
y = (1, 2)
# print(x + y) # 예외 발생

# 예외 처리 기본
# try: 에러가 발생할 가능성이 있는 코드 실행
# except: 에러명1
# except: 에러명2
# else: 에러가 발생하지 않았을 경우 실행
# finally: 항상 실행

# 예제1
name = ['Kim', 'Lee', 'Park']
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! = Occurred ValueError!')
except IndexError:
    print('Not found it! = Occurred IndexError!')
except Exception:
    print('Not found it! = Occurred Error!')
else:
    print('Ok! else!')


# 예제2
try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except Exception:
    print('Not found it! = Occurred Error!')
else:
    print('Ok! else!')


# 예제3
try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! = Occurred Error!')
else:
    print('Ok! else!')
finally:
    print('finally ok!')

# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print('Ok Finally!!!')

# 예제5
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a == 'Lee':
        print('OK 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('Ok!')

