# 문자열, 문자열 연산, 슬라이싱
str1 = "I am Boy."
str2 = "NiceMan"
str3 = ''
str4 = str('a')

print(len(str1), len(str2), len(str3), len(str4))  # 9 7 0 1

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)  # Do you have a "big collection"
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String, 주로 경로 문자열에 사용
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)  # C:\Programs\Test\Bin
raw_s2 = r"\\a\\a"
print(raw_s2)  # \\a\\a

# 멀티라인
multi = \
    """ 
문자열
멀티라인
테스트
"""
print(multi)

# 문자열 연산
str_o1 = "*"
str_o2 = "abc"
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print('a' in str_o4)  # True
print('a' not in str_o4)  # False

# 문자열 형 변환
print(str(77) + 'a')  # 77a
print(str(10.4))  # 10.4

# 문자열 함수
# a = 'niceman'
# b = 'orange'
#
# print(a.islower()) # True
# print(b.endswith('e')) # True
# print(a.capitalize()) # Niceman
# print(a.replace('nice', 'good')) # goodman
# print(list(reversed(b))) # ['e', 'g', 'n', 'a', 'r', 'o']

a = 'niceman'
b = 'orange'

print(a[0:3])  # nic
print(a[0:4])  # nice
print(a[0:])  # niceman
print(a[0:len(a)])  # niceman
print(a[:4])  # nice
print(a[:])  # niceman
print(b[0:4:2])  # oa, 2개씩 건너뜀.
print(b[1:-2])  # ran
print(b[::-1])  # egnaro, 역순으로 인덱스 작용
