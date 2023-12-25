from numpy import int32


print("Calculator with Python")
print()
num1 = int32(input("Enter the first number: "))
num2 = int32(input("Enter the second number: "))
print()
oper = input("Enter the operation want to perform: ")

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
elif oper == "/":
    print(num1 / num2)
else:
    print("Invalid Operations!")