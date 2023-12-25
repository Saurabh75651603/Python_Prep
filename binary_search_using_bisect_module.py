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

# class WorkingWithBisectUsingClass:
#     def __init__(self, arr):
#         self.arr = arr

#     def bisect_left(self, a):
#         return bisect.bisect_left(self.arr, a)

#     def bisect_right(self, a):
#         return bisect.bisect_right(self.arr, a)

# # Example usage of the class
# sorted_list_class = [12, 34, 45, 56, 67, 78, 89, 90]
# calling_class = WorkingWithBisectUsingClass(sorted_list_class)

# index_left_class = calling_class.bisect_left(42)
# index_right_class = calling_class.bisect_right(81)

# print(f"Index to insert 42 (class bisect_left): {index_left_class}")
# print(f"Index to insert 81 (class bisect_right): {index_right_class}")

import bisect

num = int(input("Enter a number you want to insert in between this list: "))

class BisectModuleInClass:
    
    def __init__(self, arr_list):
        self.arr_list = arr_list
        
    def bisect_left(self, num):
        return bisect.bisect_left(self.arr_list, num)
    
    def bisect_right(self, num):
        return bisect.bisect_right(self.arr_list, num)

arr_list = [12, 23, 34, 45, 56, 67, 78, 89, 90]
class_calling = BisectModuleInClass(arr_list)

# Check if the entered number is greater than the length of the list
if num > len(arr_list):
    print(f"The {num} can be added at the end of the list.")

# Use the class methods to get the indices
index_left_class = class_calling.bisect_left(15)
index_right_class = class_calling.bisect_right(69)

# Check if both indices are at the end of the list
if index_left_class == index_right_class == len(arr_list):
    print(f"The number could be added at index {len(arr_list) + 1} where the list ends, i.e. after the last element {arr_list[-1]}")
else:
    print(f"The number could be added at index {index_right_class} on the behalf of replacing {arr_list[index_right_class]}.")
