#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

def inputnumber():
    first = float(input("   Enter 1st number: "))
    second = float(input("   Enter 2nd number: "))
    third = float(input("   Enter 3rd number: "))
    fourth = float(input("   Enter 4th number: "))
    return first, second, third, fourth

num1, num2, num3, num4 = inputnumber()

if num1 > num2 and num2 > num3 and num3 > num4:
    print(num1,num2,num3,num4)
elif num1> num2 and num2 > num4 and num4 > num3:
    print(num1,num2,num4,num3)
elif num1> num3 and num3>num2 and num2>num4:
    print(num1,num3,num2,num4)
elif num1> num3 and num3>num4 and num4>num2:
    print(num1,num3,num4,num2)
elif num1 >num4 and num4>num2 and num2>num3:
    print(num1,num4,num2,num3)
elif num1>num4 and num4>num3 and num3>2:
    print(num1,num4,num3,num2)

#if second number is highest
if num2>num3 and num3>num4 and num4>num1:
    print(num2,num3,num4,num1)
elif num2>num3 and num3>num1 and num1>num4:
    print(num2,num3,num1,num4)
elif num2>num4 and num4>num1 and num1>num3:
    print(num2,num4,num1,num3)
elif num2>num4 and num4>num3 and num3>num1:
    print(num2,num4,num3,num1)
elif num2>num1 and num1>num3 and num3>num4:
    print(num2,num1,num3,num4)
elif num2>num1 and num1>num4 and num4>num3:
    print(num2,num1,num4,num3)
