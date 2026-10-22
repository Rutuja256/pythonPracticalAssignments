num1=int(input("enter your first number :"))
num2=int(input("enter your second number :"))
num3=int(input("enter your third number :"))

if num1>num2 and num1>num3:
    print(num1,"is the largest number")
elif num2>num1 and num2>num3:
    print(num2,"is greater")
else:
    print(num3,"is greater")        