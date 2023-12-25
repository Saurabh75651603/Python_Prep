# a = 10
# b = 90

# if a == b:
#     try:
#         result = a+b
#     except Exception:
#         result = a - b
#     finally:
#         print(a, "this is the value of a")
#         print(b, "this is the value of b")        
# elif a < b:
#     result = a*b
# elif a > b:
#     result = a*a
# else:
#      result = a/b


# print(result)
    
a = int(input("Enter a number :"))
b = int(input("Enter a number :"))

if a == b:
    try:
        result = a + b
    except Exception:
        result = a - b
    finally:
        print("Value of a:", a)
        print("Value of b:", b)
elif a < b:
    result = a * b
elif a > b:
    result = a * a
elif a != b:
    result = b*b
else:
    result = a / b

print("Result:", result)

    







# a = 2

# b = 0

# try:
#     print(a/b)
    
# except Exception as e:
#     print("Hey, this error is due to ", e)
    
    
    
    
    
    
    
    