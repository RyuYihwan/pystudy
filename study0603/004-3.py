# 딕셔너리, 집합 자료형
# 딕셔너리(Dictionary): 순서X, 중복X, 수정O, 삭제O

# Key, Value (Json) -> MongoDB
# 선언

a = {'name': 'Kim', 'Phone': '000-0000-0000', 'birth': 901111}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

print(type(a))

print(a['name'])  # Kim
# print(a['name1']) # KeyError: 'name1'
print(a.get('name'))  # Kim
print(a.get('name1'))  # None, 좀더 안전한 형태의 출력
print(c['arr'][1:4])  # [2, 3, 4]

# 추가
a['address'] = 'Seoul'
a['rank'] = (1, 2, 3)
print(a)  # 'name': 'Kim', 'Phone': '000-0000-0000', 'birth': 901111, 'address': 'Seoul', 'rank': (1, 2, 3)}

# keys, values, items
print(a.keys())  # dict_keys(['name', 'Phone', 'birth', 'address', 'rank']), key만 가져옴
print(list(a.keys()))  # ['name', 'Phone', 'birth', 'address', 'rank']

# 리스트 형태로 변환하여 주로 사용함. 안하면 슬라이싱 등에 오류발생
temp = list(a.keys())  # ['name', 'Phone', 'birth', 'address', 'rank']
print(temp[1:3])  # ['Phone', 'birth']

print(a.values())  # dict_values(['Kim', '000-0000-0000', 901111, 'Seoul', (1, 2, 3)]), 값만 가져옴
print(list(
    a.items()))  # [('name', 'Kim'), ('Phone', '000-0000-0000'), ('birth', 901111), ('address', 'Seoul'), ('rank', (1, 2, 3))], 리스트 안의 튜플 형태
print(2 in b)  # False, key가 2 인 것이 있는지
print('name2' not in a)  # True

# 집합(Sets) (순서X, 중복X)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))  # <class 'set'>
print(c)  # {1, 4, 5, 6}

# 형변환
t = tuple(b)
print(t)  # (1, 2, 3, 4)
l = list(b)
print(l)  # [1, 2, 3, 4]

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))  # {4, 5, 6}, 교집합
print(s1 & s2)  # {4, 5, 6}, 교집합

print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}, 합집합
print(s1 | s2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}, 합집합

print(s1 - s2)  # {1, 2, 3}, 차집합
print(s1.difference(s2))  # {1, 2, 3}, 차집합

# 추가 & 제거
s3 = set([7, 8, 9, 10, 15])
s3.add(18)
# s3.add(7)
print(s3)  # {7, 8, 9, 10, 15, 18}

s3.remove(15)
print(s3)  # {7, 8, 9, 10, 18}

print(type(s3))  # <class 'set'>
