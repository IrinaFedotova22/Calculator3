import math
import random
print('Welcome to calculator!')


class Calculator:
    def __init__(self, first_num):
        self.first_num = first_num
        self.second_num = 0

    def addition(self):
        second_num = (int(input("Enter the 2nd number:")))
        return self.first_num + second_num

    def subtraction(self):
        second_num = (int(input("Enter the 2nd number:")))
        return self.first_num - second_num

    def division(self):
        second_num = (int(input("Enter the 2nd number:")))
        if second_num != 0:
            return self.first_num / second_num
        else:
            print("This is an invalid input")

    def multiplication(self):
        second_num = (int(input("Enter the 2nd number:")))
        return self.first_num * second_num

    def raising_to_the_power_of(self):
        second_num = (int(input("Enter the 2nd number:")))
        return self.first_num ** second_num

    def absolute_value(self):
        return abs(self.first_num)

    def factorial(self):
        return math.factorial(self.first_num)

    def arccos(self):
        return math.acos(self.first_num)

    def divine_random(self):
       second_num = (int(input("Enter the 2nd number:")))
       return random.uniform(self.first_num, second_num)

    def get_expression(self, operation):
        if operation == '+':
            return self.addition()
        elif operation == '-':
            return self.subtraction()
        elif operation == '/':
            return self.division()
        elif operation == '*':
            return self.multiplication()
        elif operation == '**':
            return self.raising_to_the_power_of()
        elif operation == '||':
            return self.absolute_value()
        elif operation == '!':
            return self.factorial()
        elif operation == 'arccos':
            return self.arccos()
        elif operation == 'R':
            return self.divine_random()
        else:
            print("This is an invalid input")

while True:

    operation = input("Enter your operation: ")
    user_num1 = (int(input("Enter the 1st number:")))
    get_expression = operation

    calc = Calculator(user_num1)
    res = calc.get_expression(get_expression)
    print(res)

    calculation = input("Continue the calculation?: ")

    if calculation == 'yes':
        continue
    else:
        break
