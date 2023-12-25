# Binary Search using Iterative Approach

pos = -1

def binary_search(arr_item, search_item):
    
    lower_bound = 0
    upper_bound = len(arr_item) - 1
    
    while lower_bound <= upper_bound:
        mid_item = (lower_bound + upper_bound) // 2    # Returns int division
        
        if arr_item[mid_item] == search_item:
            pos = mid_item 
            return True
        else:
            if arr_item[mid_item] < search_item:
                lower_bound = mid_item +1
            else:
                upper_bound = mid_item -1
                
arr_item = [12,23,34,45,56,67,78,89,90]
search_item = 34

if binary_search(arr_item, search_item):
    print("Found at ", pos +1 )
else:
    print("Not Found")
 

   
# pos = -1

# def binary_search(arr_item, search_item):
#     global pos
#     lower_bound = 0
#     upper_bound = len(arr_item) - 1
    
#     while lower_bound <= upper_bound:
#         mid_item = (lower_bound + upper_bound) // 2
        
#         if arr_item[mid_item] == search_item:
#             pos = mid_item 
#             return True
#         else:
#             if arr_item[mid_item] < search_item:
#                 lower_bound = mid_item + 1
#             else:
#                 upper_bound = mid_item - 1
                
#     return False

# arr_item = [12, 23, 34, 45, 56, 67, 78, 89, 90]
# search_item = 34

# if binary_search(arr_item, search_item):
#     print("Found at", pos + 1)
# else:
#     print("Not Found")
