import os


banner = """
Python Calculator -Bimzzx
Thanks for : Hanz a.k.a forbidden
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


def add(num1, num2):
   return num1 + num2

def subtract(num1, num2):
   return num1 - num2

def multiply(num1, num2):
   return num1 * num2

def divide(num1, num2):
   return num1 / num2

def tothepowerof(num1, num2):
    result = pow(num1, num2)
    return result

def remainderofdivision(num1, num2):
    return num1 % num2

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    select = int(input('┌───── SELECT OPTIONS\n└───> '))
    if select == 0:
        exit()
    elif select == 1:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        print(f"┌───── RESULTS\n└──> {add(num1,num2)}")
    elif select == 2:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        print(f"┌───── RESULTS\n└──> {subtract(num1,num2)}")
    elif select == 3:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        print(f"┌───── RESULTS\n└──> {multiply(num1,num2)}")
    elif select == 4:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        print(f"┌───── RESULTS\n└──> {divide(num1,num2)}")
    elif select == 5:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        print(f"┌───── RESULTS\n└──> {tothepowerof(num1,num2)}")
    elif select == 6:
        num1 = int(input("┌───── INPUT NUMBERS\n└[1]──> "))
        num2 = int(input("┌───── INPUT NUMBERS\n└[2]──> "))
        print(f"┌───── RESULTS\n└──> {remainderofdivision(num1,num2)}")
    else:
        print('Please enter the options correctly!')

main()