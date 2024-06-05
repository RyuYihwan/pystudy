# 조건문
# 관계연산자
a = 10
b = 0
print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a >= b)  # True
print(a < b)  # False
print(a <= b)  # False

# 참 거짓 종류(True, False)
# 참 : "내용", [내용], (내용), {내용}, 1, True
# 거짓 : "", [], (), {}, 0, False
print("=====================")
city = ""  # False
if city:
    print("True")
else:
    print("False")

# 논리 연산자
# and or not
a = 100
b = 60
c = 15

print('and :', a > b and b > c)  # and : True
print('or :', a > b or c > b)  # or : True
print('not :', not a > b)
print(not False)  # True
print(not True)  # False

# 산술 > 관계 > 논리 순서로 적용
print('ex1 : ', 5 + 10 > 0 and not 7 + 3 == 10)  # False

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':  # 합격하셨습니다.
    print("합격하셨습니다.")
else:
    print("죄송합니다. 불합격입니다.")

# 다중조건문
num = 70  # num 등급 C 70

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("꽝")


# 중첩조건문
age = 19
height = 175
# 20세 이상 지원 가능
if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")

#