#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

def inputnumber():
    first = int(input("   Enter 1st number: "))
    second = int(input("   Enter 2nd number: "))
    third = int(input("   Enter 3rd number: "))
    fourth = int(input("   Enter 4th number: "))
    return first, second, third, fourth

num1, num2, num3, num4 = inputnumber()

#if first number is highest
if num1>num2>num3>num4:
    print(num1,num2,num3,num4)
elif num1>num2>num4>num3:
    print(num1,num2,num4,num3)
elif num1>num3>num2>num4:
    print(num1,num3,num2,num4)
elif num1>num3>num4>num2:
    print(num1,num3,num4,num2)
elif num1>num4>num2>num3:
    print(num1,num4,num2,num3)
elif num1>num4>num3>2:
    print(num1,num4,num3,num2)

#if second number is highest
if num2>num3>num4>num1:
    print(num2,num3,num4,num1)
elif num2>num3>num1>num4:
    print(num2,num3,num1,num4)
elif num2>num4>num1>num3:
    print(num2,num4,num1,num3)
elif num2>num4>num3>num1:
    print(num2,num4,num3,num1)
elif num2>num1>num3>num4:
    print(num2,num1,num3,num4)
elif num2>num1>num4>num3:
    print(num2,num1,num4,num3)

#if third number is highest
if num3>num4>num1>num2:
    print(num3,num4,num1,num2)
elif num3>num4>num2>num1:
    print(num3,num4,num2,num1)
elif num3>num1>num2>num4:
    print(num3,num1,num2,num4)
elif num3>num1>num4>num2:
    print(num3,num1,num4,num2)
elif num3>num2>num1>num4:
    print(num3,num2,num1,num4)
elif num3>num2>num4>num1:
    print(num3,num2,num4,num1)

#if the fourth num is highest
if num4>num1>num2>num3:
    print(num4,num1,num2,num3)
elif num4>num1>num3>num2:
    print(num4,num1,num3,num2)
elif num4>num2>num3>num1:
    print(num4,num2,num3,num1)
elif num4>num2>num1>num3:
    print(num4,num2,num1,num3)
elif num4>num3>num1>num2:
    print(num4,num3,num1,num2)
elif num4>num3>num2>num1:
    print(num4,num3,num2,num1)
