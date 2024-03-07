num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))
num3 = int(input("how many numbers do you want to skip: "))

for i in range(num1,num2,num3):
    print(i)