# 파이썬 클래스
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 서로 다른 것.
# 클래스 변수: 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수: 객체마다 별도로 존재, 인스턴스 생성 후 사용
# 네임스페이스: 객체를 인스턴스화 할 때 저장된 공간

# 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제1
class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
        self.name = name

    def user_info_p(self):
        print("Name: ", self.name)


user1 = UserInfo('Kim')  # 초기화
print(user1.name)  # Kim
user1.user_info_p()  # Name:  Kim
user2 = UserInfo("Park")
print(user2.name)  # Park
user2.user_info_p()  # Name:  Park

# namespace 출력
print(user1.__dict__)  # {'name': 'Kim'}
print(user2.__dict__)  # {'name': 'Park'}


# 예제2
# self의 이해
class SelfTest():
    def function1():
        print('function1 called')

    def function2(self):
        print(id(self))
        print('function2 called')


self_test = SelfTest()
# self_test.function1(), 여러 인스턴스가 공유하는 함수이므로(self 없음) 에러 발생
SelfTest.function1()  # function1 called
self_test.function2()  # function2 called

print(id(self_test))  # 1989297586920, function2 내부에서 호출한 self의 id와 동일
SelfTest.function2(self_test)  # 인스턴스 대입하지 않으면 self 없어서 에러 발생, 위의 출력값과 id 동일.


# 예제 3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)  # {'name': 'Kim'}
print(user2.__dict__)  # {'name': 'Park'}
print(user3.__dict__)  # {'name': 'Lee'}
print(WareHouse.__dict__)  # 'stock_num': 3, 이 포함된 값을 출력함. 클래스 변수(공유)

print(user1.stock_num)  # 3, 클래스의 네임스페이스에서 찾아옴.
print(user2.stock_num)  # 3
print(user3.stock_num)  # 3

del user1

print(user2.stock_num)  # 2
print(user3.stock_num)  # 2
