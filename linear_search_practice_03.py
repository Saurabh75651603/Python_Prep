# names = ['Saurabh', 'Anushka', 'Aditya', 'Sameer' , 'Sana']

# j_names = []

# for name in names:
#     if 'S' in name:
#         j_names.append(name)
        
# for name in names:
#     if 'A' in name:
#         j_names.append(name)
        
# print(j_names)
# print(j_names)

# j_names = [name for name in names if 'S' in name]            # List-Comprehension method
# print(j_names)


# j_names = [name for name in names if 'A' in name]            # List-Comprehension method
# print(j_names)



def linear_search(list_item, target_item):
    
    i = 0
    while i <len(list_item):
        if list_item[i] == target_item:
            return 1
        i +=1
    return -1

list_item = [21,24,53,76,24,57,23]
target_item = 53
result = linear_search(list_item, target_item)

if result == 1:
    print("found!")
else:
    print("Not Found") 
    
    
    
    
def linear_search_with_list_comprehension(arr, search_item):
    
    indices = [i for i, x in enumerate(arr) if x == search_item]
    return indices[0] if indices else -1


arr_item = [21,3,64,4,46,67,3,4]
search_item = 67
result_item = linear_search_with_list_comprehension(arr_item, search_item)

if result_item != -1:
    print(f"Element {search_item} found at index {result_item}.")
else:
    print(f"Element {search_item} not found in the list.")


'''
Incomplete comprehension method
missed defining 'x' (element in arr_item), and mistake in comparision format.
'''

def linear_search_with_list_comprehension(arr, target):
    
    indices = [i for i, x in enumerate(arr) if x == target]
    return indices[0] if indices else -1

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 5

result = linear_search_with_list_comprehension(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")



# Linear Search using Enumerate method

arr_item = [32,5,23,56,567,43,56,76,23,754,42,53,786,9886]
print(arr_item)
# search_item = 42

# result_item = linear_search_using_enumerate_method(arr_item, search_item)


Num = int(input("Enter the number from the given array you want to search for: "))


Found = False

# def linear_search_using_enumerate_method(arr_item, target_item):
    
for i, element in enumerate(arr_item):
    if Num == element:
        Found = True
        break
       
# result_item = linear_search_using_enumerate_method(arr_item, search_item)

if Found:
    print("File_Handling13.py")
else:
    print("Multi-Threading12.py")