# def binary_search_using_recursive_function(arr, target, low, high):
    
#     low = 0
#     high = len(arr) -1
#     if low <= high:
#         mid = (low+high) //2
#         if arr[mid] == target:
#             return mid
#         elif loarr[mid] > target:
#             return binary_search_using_recursive_function(arr, target, low, mid -1)
#         else:
#             return binary_search_using_recursive_function(arr, target, low, mid +1)
#     else:
#         return -1


# def binary_search_using_recursive_function(arr, target, low, high):
    
#     low = 0
#     high = len(arr)-1
    
#     if low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             return binary_search_recursive(arr, target, low, mid - 1)
#         else:
#             return binary_search_recursive(arr, target, mid + 1, high)
#     else:
#         return -1  # Target not found

# arr = [12,34,45,56,67,78,79,89,90]
# target = 78
# result = binary_search_using_recursive_function(arr, target, low, high)

# if result == 1:
#     print("The number found at {result}")
# else:
#     print("The number not found")
    
    
    
# from bisect import *
# def binary_search_using_bisect_module(arr, target):
    
#     index = bisect.bisect_left(arr, target)
#     if index < len(arr) and arr[index] == target:
#         return index
#     else:
#         return -1
    

# arr = [12,34,45,56,67,78,79,89,90]
# target = 78
# result = binary_search_using_bisect_module(arr, target, low, high)

# if result == 1:
#     print("The number found at {result}")
# else:
#     print("The number not found")
    
    
import bisect

sorted_list = [12,34,45,56,67,78,89,90]

index = bisect.bisect_left(sorted_list, 100)

print(f"Index to insert 78:{index}")

import bisect

sorted_list = [12,34,45,56,67,78,89,90]

index = bisect.bisect_left(sorted_list, 39)

print(f"The given element can be inserted at:{index}")


# if index = bisect.bisect_left():
#     print("The number can be placed left side of the ")
    
    
    
# import bisect

# Num = int(input("Enter the sorted list of numbers: "))

# sorted_list = [12,34,45,56,67,78,89,90]

# index = bisect.bisect_left(sorted_list,Num)

# print(f"The number could be added at {index}")

# import bisect

# sorted_list = [12, 34, 45, 56, 67, 78, 89, 90]

# # Assuming Num is an integer input
# Num = int(input("Enter the number: "))

# index = bisect.bisect_right(sorted_list, Num)

# if index == len(sorted_list):
#     print(f"The number {Num} could be added at the end of the list.")
# else:
#     print(f"The number {Num} could be added at index {index} on the behalf of replacing {index}.")


# import bisect

# sorted_list = [12, 34, 45, 56, 67, 78, 89, 90]

# # Assuming Num is an integer input
# Num = int(input("Enter the number: "))

# index = bisect.bisect_right(sorted_list, Num)

# if index == len(sorted_list):
#     print(f"The number {Num} could be added at the end of the list.")
# else:
#     print(f"The number {Num} could be added at index {index} on the behalf of replacing {sorted_list[index]}.")
#     # print(f"The number at index {index} is {sorted_list[index]}.")

# import bisect

# class working_with_bisect_using_class:
    
#     def __init__(self, arr):
#         self.arr = arr
        
#     def bisect_left(self, a):
#         return bisect.bisect_left(self.arr, a)
    
#     def bisect_right(self, a):
#         return bisect.bisect_right(self.arr, a)
    
# sorted_list = [12,34,45,56,67,78,89,90]
# calling_class = working_with_bisect_using_class(sorted_list)

# index_left_class = calling_class.bisect_left (42)
# index_right_class = calling_class.bisect_right (81)

# print(f"Index to insert 42 (class bisect_left): {index_left_class}")
# print(f"Index to insert 81 (class bisect_right): {index_right_class}")



# Incorrect one 

import bisect

print("arr_list = [12,23,34,45,56,67,78,89,90]")
num = int(input("Enter a number you want to insert in between this list: ",))

class bisect_module_in_class:
    
    def __init__(self, arr_list):
        self.arr_list = arr_list
        
    def bisect_left(self, num):
        return bisect.bisect_left(self.arr_list, num)
    
    def bisect_right(self, num):
        return bisect.bisect_right(self.arr_list, num)
    

arr_list = [12,23,34,45,56,67,78,89,90]
class_calling = bisect_module_in_class(arr_list)

for element in arr_list:
    if num > len(arr_list):
        print(f"The number {num} can be placed at the end of the given list")

index_left_class = class_calling.bisect_left(15)
index_right_class = class_calling.bisect_right(69)

if index_left_class and index_right_class == len(arr_list):
    print(f"The number could be added at index {len(arr_list) + 1} on the behalf of replacing {arr_list[index]}")
else:
    print(f"The number cannot be added in the given list.")
    
    
