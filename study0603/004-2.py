# 리스트, 튜플

# 리스트(순서O, 중복O, 수정O, 삭제O)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[0] + d[1])  # 110
print(d[3])  # 전부 바나나
print(d[-1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:2])  # [10, 100]
print(e[2][1:3])  # ['Banana', 'Orange']

# 연산
print(c + d)  # [1, 2, 3, 4, 10, 100, 'Pen', 'Banana']
print(c * 3)  # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(str(c[0]) + 'hi')  # 1hi

# 리스트 수정, 삭제
c[0] = 77
print(c)  # [77, 2, 3, 4]

c[1:2] = [100, 1000, 10000]
print(c)  # [77, 100, 1000, 10000, 3, 4]

c[1] = ['a', 'b', 'c']
print(c)  # [77, ['a', 'b', 'c'], 1000, 10000, 3, 4]

del c[1]
print(c)  # [77, 1000, 10000, 3, 4]
del c[-1]
print(c)  # [77, 1000, 10000, 3]
print('=======================')

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)  # [5, 2, 3, 1, 4]
y.append(6)
print(y)  # [5, 2, 3, 1, 4, 6]
y.sort()
print(y)  # [1, 2, 3, 4, 5, 6]
y.reverse()
print(y)  # [6, 5, 4, 3, 2, 1]
y.insert(2, 7)
print(y)  # [6, 5, 7, 4, 3, 2, 1]
y.remove(2)  # 값을 기준으로 삭제
print(y)  # [6, 5, 7, 4, 3, 1]
y.pop()  # 마지막 값 삭제
print(y)  # [6, 5, 7, 4, 3]
ex = [88, 77]
y.extend(ex)
print(y)  # [6, 5, 7, 4, 3, 88, 77]
# y.append(ex) # [6, 5, 7, 4, 3, [88, 77]]

# 튜플(순서O, 중복O, 수정X, 삭제X)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])  # 3
print(c[3])  # 4
print(d[2][1])  # b

print(d[2:])  # (('a', 'b', 'c'),)
print(d[2][0:2])  # ('a', 'b')

print(c + d)  # (1, 2, 3, 4, 10, 100, ('a', 'b', 'c'))
print(c * 3)  # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

z = (5, 2, 1, 3, 1)

print(z)  # (5, 2, 1, 3, 4)
print(3 in z)  # True
print(z.index(5))  # 0, 값 기준 인덱스 반환
print(z.count(1))  # 2
