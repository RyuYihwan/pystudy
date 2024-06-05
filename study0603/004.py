# 데이터 타입

v_str1 = "Niceman"
v_bool = "True"
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name": "Kim",
    "age": 25
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_tuple))  # <class 'tuple'>
print(type(v_set))  # <class 'set'>
print(type(v_float))  # <class 'float'>

i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999
big_int2 = 77777777777777777777777777
f1 = 1.234
f2 = 3.239
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
result = f3 + i2  # 실수로 자동 형변환
print(result, type(result))  # 939.5 <class 'float'>

# 형변환
# int, float, complex(복소수)
a = 5.
b = 4
c = 10
print(type(a), type(b))  # <class 'float'> <class 'int'>
result2 = a + b
print(result2, int(result2))  # 9.0 9
print(int(result2))  # 9
print(float(c))  # 10.0
print(complex(3))  # (3+0j)
print(int(True))  # 1
print(int(False))  # 0
print(int('3'))  # 3
print(complex(False))  # 0j

# 기본연산
y = 100
y *= 100
print(y)  # 10000

# 수치 연산 함수
print(abs(-7))  # 7
n, m = divmod(100, 8)
print(n, m)  # 12 4

import math

print(math.ceil(5.1))  # 6
print(math.floor(5.1))  # 5
