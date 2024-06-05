# 함수
# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요
# 호출전에 선언해야 된다.
# 예제 1
def hello(s):
    print("Hello ", s)


hello("Python")
hello(777)


# 예제 2
def hello_return(s):
    val = "Hello " + str(s)
    return val


s = hello_return("Python!!!")
print(s)


# 예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(100)
print(val1, val2, val3)  # 10000 20000 30000


# 예제4(데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = func_mul2(100)
print(lt, type(lt))  # [10000, 20000, 30000] <class 'list'>


# 예제5
# *args, *kwargs

def args_func(*args):
    print(args)
    # for i, v in enumerate(args): -> 인덱스, 값을 출력 가능
    #     print(i, v)


args_func('Kim')  # ('Kim',)
args_func('Kim', 'Park', 'Lee')  # ('Kim', 'Park', 'Lee')
args_func('Kim', 'Park', 'Lee', 'Sun')  # ('Kim', 'Park', 'Lee', 'Sun')


def kwargs_func(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():  # key-value 형태로 출력
        print(k, v)


kwargs_func(name1='Kim')  # {'name1': 'Kim'}
kwargs_func(name1='Kim', name2='Park', name3='Lee')  # {'name1': 'Kim', 'name2': 'Park', 'name3': 'Lee'}


# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)  # 10 20 () {}
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)  # 10 20 ('park', 'kim') {'age1': 24, 'age2': 35}


# 중첩함수(클로저)

def nested_func(num):
    def func_in_func(num2):
        print('>>>>', num2)

    print("in func")
    func_in_func(num + 10000)


nested_func(10000)


# in func
# >>>> 20000

# 함수 hint
def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul3(5))  # [500, 1000, 1500]


# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리)할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func)  # <function mul_10 at 0x0000026793294F28>
print(type(var_func))  # <class 'function'>

print(var_func(10))  # 100

lambda_mul_10 = lambda num: num * 10

print('>>>', lambda_mul_10(10))  # >>> 100


def func_final(x, y, func):
    print(x * y * func(10))


func_final(10, 10, lambda_mul_10)  # 10000
