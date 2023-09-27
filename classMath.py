class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        res = self.a + self.b
        print(f"Ответ {res}")
    def substraction(self):
        res = self.a - self.b
        print(f"Ответ {res}")
    def multiplication(self):
        res = self.a * self.b
        print(f"Ответ {res}")
    def division(self):
        if self.b !=0:
            res = self.a / self.b
            print(f"Ответ {res}")
        else:
            print("На ноль делить нельзя")
a = float(input("Первое число: "))
b = float(input("Второе число: "))
math_obj = Math(a,b)
math_obj.addition()
math_obj.division()
math_obj.multiplication()
math_obj.substraction()