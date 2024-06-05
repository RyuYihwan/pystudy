# 반복문: for, while

v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):  # 10 미만까지 반복
    print("v2 is :", v2)

for v3 in range(1, 11):  # 1부터 10 미만까지 반복
    print("v3 is :", v3)

# 1 ~ 100 합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100: ', sum1)  # 1 ~ 100:  5050
print('1 ~ 100: ', sum(range(1, 101)))  # 1 ~ 100:  5050
print('1 ~ 100: ', sum(range(1, 101, 2)))  # 1 ~ 100:  2500, 2씩 건너뛴다.

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable : range, reversed, enumerate, filter, map, zip

names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

for name in names:
    print("You are : ", name)

word = "dreams"
for s in word:
    print("Word : ", s)

my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}
# 기본값: 키
for key in my_info:
    print("my_info", key)
# 값
for value in my_info.values():
    print("my_info", value)
# 키
for key in my_info.keys():
    print("my_info", key)
# 키 and 값
for k, v in my_info.items():
    print("my_info", k, v)

name = "KennRY"

for n in name:
    if n.isupper():  # 대문자 -> 소문자로
        print(n.lower())
    else:  # 소문자 -> 대문자로
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 20, 24, 7, 22]
for num in numbers:
    if num == 20:
        print("found: 20!")
        break
    else:
        print("not found : 20!")

# for - else 구문(반복문이 정상적으로 수행된 경우 else 블럭 수행)
for num in numbers:
    if num == 20:
        print("found: 20!")
        # break
    else:
        print("Not found : 20!")
else:
    print("Not found 20.....")  # break 구문이 없으면 맨 마지막에 실행

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입: ", type(v))

name = "Niceman"
print(reversed(name))  # <reversed object at 0x000001EB0BB4C2B0>
print(list(reversed(name)))  # ['n', 'a', 'm', 'e', 'c', 'i', 'N']
print(tuple(reversed(name)))  # ('n', 'a', 'm', 'e', 'c', 'i', 'N')

# list comprehension
# x = [x for x in 이터러블 if 조건문]

numbers = []
for n in range(1, 101):
    numbers.append(n)
print(numbers)

numbers2 = [x for x in range(1, 101)]
print(numbers2)

q = ["갑", "정", "병", "을"]
result = [x for x in q if x != "정"]
print(result)  # ['갑', '병', '을']

# 홀수만의 배열
q1 = [x for x in range(1, 101) if x % 2 != 0]
print(q1)

