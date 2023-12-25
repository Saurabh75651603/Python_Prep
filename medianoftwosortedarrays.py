# def medianoftwosortedarrays (self, num1, num2):
    
#     n = len(num1)
#     m = len(num2)
    
#     def addtwosortedarrays(self, num1, num2):
#         add1 = num1 + num2
#         return add1
    
# num1 = [2,6,9,14,46]
# num2 = [23,34,56,68]

# add2 = 

# add = medianoftwosortedarrays(num1+num2)//2
# print(add)


def medianoftwosortedarrays(num1, num2):
    combined = sorted(num1 + num2)
    n = len(combined)

    if n % 2 == 0:
        # If the combined length is even, take the average of the middle two elements
        return (combined[n // 2 - 1] + combined[n // 2]) / 2
    else:
        # If the combined length is odd, return the middle element
        return combined[n // 2]

num1 = [2, 6, 9, 14, 46]
num2 = [23, 34, 56, 68]

median = medianoftwosortedarrays(num1, num2)
print(median)
