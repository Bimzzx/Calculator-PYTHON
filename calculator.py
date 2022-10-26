import os, sys


banner = """
Python Calculator -Bimzzx
┌──────────────────────────────────────┐
│        [0]. Exit                     │
│        [1]. Plus                     │
│        [2]. Minus                    │
│        [3]. Multiplication           │
│        [4]. Divided                  │
│        [5]. To the power of          │
│        [6]. Remainder of division    │
└──────────────────────────────────────┘
"""

class Calculator:

    def add(num1, num2):
        return num1 + num2
    
    def subtract(num1, num2):
        return num1 - num2
    
    def multiply(num1, num2):
        return num1 * num2
    
    def divide(num1, num2):
        return num1 / num2

    def tothepowerof(num1, num2):
        return pow(num1, num2)
    
    def remainderofdivision(num1, num2):
        return num1 % num2


def question() :
    choose = input('Do you want to repeat (Y/N)? ')
    if choose == 'Y' or choose == 'y':
         main()
    elif choose == 'N' or choose =='n':
        print('Thank you :)')
        sys.exit()
    else :
        print('Please enter the options correctly! (y/n) \n')
        question()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    select = int(input('┌───── SELECT OPTIONS\n└───> '))
    if select == 0:
        sys.exit()
    elif select == 1:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        result = Calculator.add(num1, num2)
        print(f"\n┌───── RESULTS\n└──> {result}")
        question()
    elif select == 2:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        result = Calculator.subtract(num1, num2)
        print(f"\n┌───── RESULTS\n└──> {result}")
        question()
    elif select == 3:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        result = Calculator.multiply(num1, num2)
        print(f"\n┌───── RESULTS\n└──> {result}")
        question()
    elif select == 4:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        result = Calculator.divide(num1, num2)
        print(f"\n┌───── RESULTS\n└──> {result}")
        question()
    elif select == 5:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        result = Calculator.tothepowerof(num1, num2)
        print(f"\n┌───── RESULTS\n└──> {result}")
        question()
    elif select == 6:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        result = Calculator.remainderofdivision(num1, num2)
        print(f"\n┌───── RESULTS\n└──> {result}")
        question()
    else:
        print('Please enter the options correctly!')

main()
