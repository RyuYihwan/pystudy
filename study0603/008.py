# 파이썬 모듈, 패키지

# 사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233

print("ex1: ", Fibonacci.fib2(300))  # ex1:  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
print("ex1: ", Fibonacci().title)  # ex1:  fibonacci

# 사용2(클래스, 비권장)
# 필요한 것만 import 하는 것이 좋다.
# from pkg.fibonacci import *

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(300)

print("ex3: ", fb.fib2(300))  # ex3:  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
print("ex3: ", fb().title)  # ex3:  fibonacci

# 사용4(함수)
import pkg.cal as c

print("ex4: ", c.add(10, 100))  # ex4:  110
print("ex4: ", c.mul(10, 100))  # ex4:  1000

# 사용5(함수, 권장)
from pkg.cal import add as a

print(a(1, 2))  # 3

# 사용6
import pkg.prints as p

p.prt1()  # prt1
