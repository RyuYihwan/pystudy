# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

class Car:
    """Parent Class"""

    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'


class BmwCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')
print(model1.color)  # Super
print(model1.type)  # Super
print(model1.car_name)  # Sub
print(model1.show())  # Super
print(model1.show_model())  # Sub
print(model1.__dict__)  # {'type': 'sedan', 'color': 'red', 'car_name': '520d'}

# Method Overriding(오버라이딩)
model2 = BenzCar("220d", 'suv', 'black')
print(model2.show())  # Sub

# Parent Method Call -> super() 활용
model3 = BenzCar("350s", 'sedan', 'silver')
print(model3.show())

# Inheritance Info
print(BmwCar.mro())  # [<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]
print(BenzCar.mro())  # [<class '__main__.BenzCar'>, <class '__main__.Car'>, <class 'object'>]


# 다중 상속
class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(A, B):
    pass


print(M.mro())  # 복잡한 상속은 지양할 것.
print(A.mro())  # [<class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>]
