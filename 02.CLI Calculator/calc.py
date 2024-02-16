# CLI calculator
import math


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        return "Error! Division by zero"
    return num1 / num2


def fact(num):
    return 1 if num == 0 or num == 1 else num * fact(num - 1)


def modulo(num1, num2):
    return int(num1 % num2)


def trigon(x):
    print("1:sin")
    print("2:cos")
    print("3:tan")
    trig_fun = input("select option : ")
    if trig_fun == "1":
        print(f"sin({x}) = {format(math.sin(math.radians(x)), '.5f')}")
    elif trig_fun == "2":
        print(f"cos({x}) = {format(math.cos(math.radians(x)), '.5f')}")
    elif trig_fun == "3":
        print(f"tan({x} = {format(math.tan(math.radians(x)), '.5f')}")
    else:
        print("Invalid option selected!")


while True:
    print("=" * 10)
    print("Calculator")
    print("=" * 10)
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Factorial")
    print("6: Modulo")
    print("7: Trigonometric operations")
    print("8: Quit")
    print("-" * 10)

    option = input("select option : ")
    if option == "8":
        print("Exiting program...!")
        break
    if option in ("1", "2", "3", "4", "6", "8"):
        x = float(input("enter first number : "))
        y = float(input("enter second number : "))
        if option == "1":
            print(f"{x}+{y} = {add(x, y)}")
        elif option == "2":
            print(f"{x}+{y} = {sub(x, y)}")
        elif option == "3":
            print(f"{x}*{y} = {mul(x, y)}")
        elif option == "4":
            print(f"{x}/{y} = {div(x, y)}")
        elif option == "6":
            print(f"{x} % {y} = {modulo(x, y)}")
    elif option == "5":
        x = int(input("enter number "))
        print(f"{x}! = {fact(x)}")
    elif option == "7":
        x = float(input("Enter angle "))
        trigon(x)

    else:
        print("Invalid option selected!")
